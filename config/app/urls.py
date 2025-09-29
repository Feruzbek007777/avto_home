from django.urls import path

from .views import CarApiView

urlpatterns = [
    path('cars/', CarApiView.as_view()),
    path('cars/<int:pk>/',CarApiView.as_view()),
]