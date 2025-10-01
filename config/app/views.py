from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Cars, Driver
from .serializers import CarSerializer, DriverSerializer


class CarApiView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk:
            cars = Cars.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        else:
            try:
                car = Cars.objects.get(pk=pk)
                serializer = CarSerializer(car)
                return Response(serializer.data)
            except Exception as e :
                return Response({"message": "Bunday avtomobil mavjud emas"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = CarSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            car = serializer.save()
            return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)


class DriverApiView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk:
            drivers = Driver.objects.all()
            serializer = DriverSerializer(drivers, many=True)
            return Response(serializer.data)
        else:
            try:
                driver = Driver.objects.get(pk=pk)
                serializer = DriverSerializer(driver)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Bunday haydovchi mavjud emas"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Request, pk: int = None):
        if pk:
            return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = DriverSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            driver = serializer.save()
            return Response(DriverSerializer(driver).data, status=status.HTTP_201_CREATED)
