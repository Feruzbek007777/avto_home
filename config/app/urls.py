from django.urls import path
from .views import CarApiView, DriverApiView

urlpatterns = [
    path('cars/', CarApiView.as_view()),
    path('cars/<int:pk>/', CarApiView.as_view()),

    path('drivers/', DriverApiView.as_view()),
    path('drivers/<int:pk>/', DriverApiView.as_view()),
]
