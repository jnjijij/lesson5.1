from django.urls import path
from car_app.views import car_list, car_create, car_update, car_delete

urlpatterns = [
    path('cars/', car_list, name='car_list'),
    path('cars/create/', car_create, name='car_create'),
    path('cars/update/<int:pk>/', car_update, name='car_update'),
    path('cars/delete/<int:pk>/', car_delete, name='car_delete'),
]
