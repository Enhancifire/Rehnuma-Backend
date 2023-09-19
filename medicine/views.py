from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from rest_framework.views import Response, APIView

from .models import Medicine
from .serializers import MedicineSerializer


class MedicineView(APIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            med = Medicine.objects.all()
            serializer = MedicineSerializer(med, many=True)
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

    def post(self, request):
        try:
            serializer = MedicineSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "data": serializer.data,
                        "error": {},
                        "isSuccess": True,
                    }
                )
            else:
                return Response(
                    {
                        "data": {},
                        "error": {
                            "message": serializer.errors,
                        },
                        "isSuccess": False,
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
