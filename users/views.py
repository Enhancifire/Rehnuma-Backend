from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from rest_framework.views import Response, APIView

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileView(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = UserProfile.objects.all()
            serializer = UserProfileSerializer(user, many=True)
            return Response(
                {
                    "data": serializer.data,
                    "error": {},
                    "isSuccess": True,
                }
            )
        except Exception as e:
            print(e)
            return Response(
                {
                    "data": {},
                    "error": {
                        "message": str(e),
                    },
                    "isSuccess": False,
                }
            )
