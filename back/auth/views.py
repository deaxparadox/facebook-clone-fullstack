from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http.response import JsonResponse


from account.models import Account
from account.models.setting import Setting
from account.models.token import APIToken
from account.models.unique import Unique
from django.contrib.auth.models import User
from django.db import IntegrityError


from account.serializers.auth import LoginSerializer

@api_view(["POST"])
def login_api_view(request):
    login_serializer = LoginSerializer(data=request.data)
    
    if login_serializer.is_valid():
        uid_and_token: dict = login_serializer.login()
        
        return JsonResponse(uid_and_token, status=status.HTTP_202_ACCEPTED)
    
    return JsonResponse({"message": "Invalid login request"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    

@api_view(["GET"])
def logout_api_view(request):
    if request.method == "GET":
        return JsonResponse({"message": "welcome to logout api view"})
    
@api_view(["POST"])
def create_user_api_view(request):
    """
    Create new user, request will contain `username`, `password`,
    and `email`. 
    """
    
    # POST data
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    
    # if (
    #     len(username) == 0 or 
    #     len(email) == 0 or
    #     password is None
    # ):
    #     return Response({
    #         "message": "Invalid username and password"
    #     }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    # create user
    try:
        user = User.objects.create(username=username, email=email, password=password)
    except IntegrityError as e:
        return Response({
            "message": "Username already exist"
        }, status=status.HTTP_400_BAD_REQUEST)
        
    # create token
    try:
        token = APIToken.objects.create()
        # raise IntegrityError("Mannuay raise error while craete token")
    except IntegrityError as e: 
        user.delete()
        return Response({
            "message": "Token conflict, retry"
        }, status=status.HTTP_409_CONFLICT)
        

    # create uid
    try:
        unique = Unique.objects.create()
        # raise IntegrityError("Mannuay raise error while creating UID")
    except IntegrityError as e:
        user.delete()
        token.delete()
        return Response({
            "message": "UID conflict, retry"
        }, status=status.HTTP_409_CONFLICT)
    
    
    
    # create setting  
    setting = Setting.objects.create()

    
    # create account
    try:    
        account = Account.objects.create(user=user, token=token, setting=setting, uid=unique)
        # raise IntegrityError("Mannuay raise error while creating acount")
    except Exception as e:
        user.delete()
        token.delete()
        unique.delete()
        setting.delete()
        return Response({
            "message":  str(e)
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    return Response(
        {"message": "User {} create successfully".format(account)}, 
        status=status.HTTP_201_CREATED
    )
