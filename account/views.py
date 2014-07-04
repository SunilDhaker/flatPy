from django.contrib.auth.models import User
from rest_framework import viewsets
from account.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


@api_view(['POST' , 'GET'])
def login(request):
    message = []
    key = ''
    status = 0
    data = request.DATA
    username = None
    password = None
    try:
        username =  data['username']
        password = data['password']
    except:
        pass
    if username and password:
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                token = Token.objects.get_or_create(user=user)[0]
                token = str(token.key)
                key = token
                message.append("User is valid, active and authenticated")
                status = 1
            else:
                message.append("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            message.append("The username or password were incorrect.")
    else :
        message = 'please provide login credentials'

    return Response({"message": message , 'status': status , 'token':key})



@api_view(['POST' , 'GET'])
def register(request):
    message = []
    key = ''
    status = 0
    data = request.DATA
    username = None
    password = None
    email = None
    try:
        username =  data['username']
        password = data['password']
        email = data['email']
    except:
        pass
    if User.objects.filter(username=username).exists():
    	message = 'username already exists'
    elif username and password:
        user = User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
            # the password verified for the user
            token = Token.objects.get_or_create(user=user)[0]
            token = str(token.key)
            key = token
            message.append("User is registered successfully")
            status = 1   
        else:
            # the authentication system was unable to verify the username and password
            message.append("Sorry user couldn't be created. Please try again.")
    else :
        message = 'You provided invalid information'

    return Response({"message": message , 'status': status , 'token':key})






class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




