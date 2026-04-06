from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mock_data import PRODUCTS

class ProductListView(APIView):
    def get(self, request):
        if not request.user:
            return Response({"error": "Unauthorized"}, status=401)
        return Response(PRODUCTS)