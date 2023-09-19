from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request, format=None):
        try:
            password = request.data.get("password")
            email = request.data.get("email")

            user = User.objects.create_user(email, password)

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "data": {
                        "access": str(refresh.access_token),
                        "refresh": str(refresh),
                    },
                    "error": {},
                    "isSuccess": True,
                }
            )
        except Exception as e:
            return Response(
                {
                    "data": {},
                    "error": {"message": str(e)},
                    "isSuccess": False,
                }
            )


class UserLoginView(APIView):
    def post(self, request, format=None):
        try:
            email = request.data.get("email")
            password = request.data.get("password")

            user = authenticate(email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)

                return Response(
                    {
                        "data": {
                            "access": str(refresh.access_token),
                            "refresh": str(refresh),
                        },
                        "error": {},
                        "isSuccess": True,
                    }
                )

            else:
                return Response(
                    {
                        "data": {},
                        "error": {"message": "Invalid credentials"},
                        "isSuccess": False,
                    }
                )

        except Exception as e:
            return Response(
                {
                    "data": {},
                    "error": {"message": str(e)},
                    "isSuccess": False,
                }
            )


class UserRefreshView(APIView):
    def post(self, request):
        refreshToken = request.data.get("refresh")
        try:
            token = RefreshToken(refreshToken)
            return Response(
                {
                    "data": {
                        "access": str(token.access_token),
                        "refresh": str(token),
                    },
                    "error": {},
                    "isSuccess": True,
                }
            )

        except Exception as e:
            return Response(
                {
                    "data": {},
                    "error": {"message": str(e)},
                    "isSuccess": False,
                }
            )
