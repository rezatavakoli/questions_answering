# questions_answering
The aim of this project is helping users to find answer (or relevant slides) for their questions in te *SlideWiki* platform. Therefore, it has provided an API which gets deck-id and a query (question), and return the sorted related slides in the deck in addition to the potential answer according to the query.

To **implement** this API, we used *Django* and *cdQA* (https://cdqa-suite.github.io/cdQA-website/).


To **run** the server, you can use `python manange.py runserver`.

To **call the API**, you can send your request to:
`base-url/answer-creator/get-answers/?deck-id=<DECK-ID>&query=<QUESTION>`
  
Moreover, the **output** has the following template:
```
[
    {
        "slide_id": <SLIDE-ID1>,
        "revision_id": <REVISION-ID1>,
        "answer": <ANSWER-TEXT1>,
        "title": <TITLE-OF-THE-SLIDE1>,
        "paragraph": <PARAGRAPH-CONTAINING-THE-ANSWER1>,
        "score": <SCORE-OF-THE-ANSWER1>
    },
    {
        "slide_id": <SLIDE-ID2>,
        "revision_id": <REVISION-ID2>,
        "answer": <ANSWER-TEXT2>,
        "title": <TITLE-OF-THE-SLIDE2>,
        "paragraph": <PARAGRAPH-CONTAINING-THE-ANSWER2>,
        "score": <SCORE-OF-THE-ANSWER2>
    }  
]
```
