from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import Group
from django.db.models import Q
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import LoginSerializer, UserSerializer

# {"username":"test4123","email":"te4st@gmail.com","password":"abcd1234","user_type":"Student"}


class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # username = request.data.get("username")
        # password = request.data.get("password")
        # email = request.data.get("email")
        user_type = request.data.get("user_type")

        if user_type == "Student":
            group, _ = Group.objects.get_or_create(name="Student")
        elif user_type == "Educator":
            group, _ = Group.objects.get_or_create(name="Educator")
        else:
            return Response({"message": "invalid user type"}, status=400)

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.groups.add(group)
                token = Token.objects.create(user=user)
                json_data = serializer.data
                json_data["token"] = token.key
                login(request, user)
                return Response(json_data, status=201)

        return Response(serializer.errors, status=400)


class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        login(request, user)
        return Response(
            {"message": "logged in", "token": token.key},
            status=status.HTTP_202_ACCEPTED,
        )


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()

        logout(request)

        return Response({"message": "logged out"}, status=200)
