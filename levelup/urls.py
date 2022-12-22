from django.urls import path
from .views import restaurant_view

urlpatterns = [
    path(
      'restaurant',
      restaurant_view,
      name="restaurant"
    ),
]
