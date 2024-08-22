from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse


@api_view(["GET"])
def login_api_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "welcome to login api view"})
    

@api_view(["GET"])
def logout_api_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "welcome to logout api view"})