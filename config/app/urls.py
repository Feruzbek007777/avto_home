from django.urls import path
from .views import CarApiView, DriverApiView, CarDetailApiView

urlpatterns = [
    path('cars/', CarApiView.as_view()),
    path('cars/<int:pk>/', CarDetailApiView.as_view()),

    path('drivers/', DriverApiView.as_view()),
    path('drivers/<int:pk>/', DriverApiView.as_view()),
]
