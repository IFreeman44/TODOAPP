from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class IndexView(APIView):
    def get(self, request):
        data = {"message": "Hello! This is TODOAPP.", "documentation": "visit again"} 
        return Response(data=data, status=status.HTTP_200_OK)
