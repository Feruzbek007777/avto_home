from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView

from .models import Cars, Driver, Color
from .serializers import CarSerializer, DriverSerializer, ColorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import Permission



class IsAdultUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
# User login qigan bosa va prfilida age mavjud bo‘lsa tekshirish mumkin(Hali mukammalroq qilsak buyam
# ish beradi yani yoshini oladigan qilsak !
# Hozircha oddiy qilib faqat autentifikatsiya qilingan userga ruxsat berdim, shuyam bolaversa kere ustoz


class CarApiView(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        car = self.queryset.all()
        return car

    def get_serializer_class(self):
        if self.request.user.is_staff:
            main = CarSerializer
        else:
            main = self.serializer_class
        return main


class CarDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = [Permission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['id', 'price', 'category', 'made_year']



class DriverApiView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['id', 'age', 'experience_year']


class ColorApiView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.AllowAny]
