from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .kitapyurdu_scraper import search_kitapyurdu, search_kirmizikedi


class BookListView(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        if not title:
            return Response({'error': 'title parametresi gerekli.'}, status=400)
        results = []
        results += search_kitapyurdu(title)
        results += search_kirmizikedi(title)
        return Response(results)
