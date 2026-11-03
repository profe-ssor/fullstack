from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_portfolio(request):
    return Response({'message': 'Portfolio data'}, status=status.HTTP_200_OK)