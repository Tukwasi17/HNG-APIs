from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import HelloSerializer

# Create your views here.
class HelloAPIView(APIView):
    def get(self, request):
        serializer = HelloSerializer(data=request.query_params)
        if serializer.is_valid():
            visitor_name = serializer.validated_data.get('visitor_name')
            return Response({"message": f"Hello, {visitor_name}"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
