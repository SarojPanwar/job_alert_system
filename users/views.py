from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.serializers import RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response(
            {
                "message": "User registered successfully",
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED
        )
    return Response(
        
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(["POST"])
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(
        username = username,
        password=password
    )

    if user is None:
        return Response(
            {
                "error":"Invalid username or password."
            },
            status=status.HTTP_403_UNAUTHORIZED
        )
    token, _ = Token.objects.get_or_create(
        user = user

    )
    return Response(
        {
            "message":"Login successful",
            "token":token.key,
            "username":user.username,
            "email":user.email,
        },
        status=status.HTTP_200_OK
    )