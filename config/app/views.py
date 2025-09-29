from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Cars
from .serializers import CarSerializer

class CarApiView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk :
            cars = Cars.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        else:
            try:
                cars = Cars.objects.get(pk=pk)
                serializer = CarSerializer(cars)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Bunday sahifa mavjud emas"}, status=status.HTTP_404_NOT_FOUND)




