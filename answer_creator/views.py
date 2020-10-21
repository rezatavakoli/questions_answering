from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services import create_answers

@api_view(['GET'])
def get_answers(req):
    deck_id = int(req.GET.get("deck-id"))
    query = req.GET.get("query")
    answers = create_answers(deck_id, query)
    return Response(status=200, data=answers)
    