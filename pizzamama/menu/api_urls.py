from django.urls import path
from .import views


urlpatterns = [
    path('getPizzas/', views.api_get_pizzas),
]