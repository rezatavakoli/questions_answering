
import pandas as pd  
import pymongo
import html2text

from ast import literal_eval
from cdqa.utils.filters import filter_paragraphs
from cdqa.utils.download import download_model, download_bnpp_data
from cdqa.pipeline.cdqa_sklearn import QAPipeline
import os
import torch
from qa_backend.settings import db

os.environ["CUDA_VISIBLE_DEVICES"]=""

def create_answers(deck_id, query):
    decks_collection = db["decks"]
    slides_collection = db["slides"]
    decks = decks_collection.find({"_id": deck_id})
    target_deck = decks[0]
    author_id = target_deck["user"]
    author_slides = slides_collection.find({"user": author_id})

    df = pd.DataFrame()

    for slide in author_slides:
        revision = slide["revisions"][-1]
        usages = revision["usage"]
        for usage in usages:
            if usage["id"] == deck_id:
                content = html2text.html2text(revision["content"])
                paragraphs = content.split('\n\n')
                df = df.append({"date": revision["timestamp"], "title": revision["title"], "category": "Infromation",
                "link": "", "abstract": "", "paragraphs": paragraphs, "revision_id": revision["id"], "slide_id": slide["_id"]}, ignore_index=True)
                break


    download_model(model='bert-squad_1.1', dir='./models')

    # df = filter_paragraphs(df)
    cdqa_pipeline = QAPipeline(reader='models/bert_qa.joblib', max_df=0.95, min_df=3)
    cdqa_pipeline.fit_retriever(df)

    predictions = cdqa_pipeline.predict(query, n_predictions=5) #retriever_score_weight=0.99

    answers = []
    i = 1
    for prediction in predictions:
        slide_id = df.loc[df["title"] == prediction[1]].iloc[0]['slide_id']
        revision_id = df.loc[df["title"] == prediction[1]].iloc[0]['revision_id']
        answers.append(
            {
                "slide_id": int(slide_id),
                "revision_id": int(revision_id),
                "answer": prediction[0],
                "title": prediction[1],
                "paragraph": prediction[2],
                "score": prediction[3]
            }
        )    
        i += 1

    return answers