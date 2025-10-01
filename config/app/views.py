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


    def put(self,request, pk:int = None):
        if not pk :
            return Response({"message": f"Method {request.method} POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                cars = Cars.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = CarSerializer(instance=cars, data=request.data, partial=True if request.method == 'PATCH' else False)
            serializer.is_valid(raise_exception=True)
            product = serializer.save()
            return Response(CarSerializer(cars).data)

    def patch(self, request, pk : int = None):
        return self.put(request, pk)


    def delete(self, request:Request, pk:int = None):
        if not pk :
            return Response({"message": "Method Delete not allowed "}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                product = Cars.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Product topilmadi"}, status=status.HTTP_404_NOT_FOUND)

            product.delete()
            return Response({"message": "Product deleted !!!"}, status=status.HTTP_204_NO_CONTENT)


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

    def put(self,request, pk:int = None):
        if not pk :
            return Response({"message": f"Method {request.method} POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                drivers = Driver.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = DriverSerializer(instance=drivers, data=request.data, partial=True if request.method == 'PATCH' else False)
            serializer.is_valid(raise_exception=True)
            drivers = serializer.save()
            return Response(DriverSerializer(drivers).data)

    def patch(self, request, pk : int = None):
        return self.put(request, pk)


    def delete(self, request:Request, pk:int = None):
        if not pk :
            return Response({"message": "Method Delete not allowed "}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                drivers = Driver.objects.get(pk=pk)
            except Exception as e:
                return Response({"message": "Driver topilmadi"}, status=status.HTTP_404_NOT_FOUND)

            drivers.delete()
            return Response({"message": "Product deleted !!!"}, status=status.HTTP_204_NO_CONTENT)

