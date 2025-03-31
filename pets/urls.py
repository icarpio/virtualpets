from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_dashboard, name='pet_dashboard'),  # Cambiado de ver_mascotas a pet_dashboard
    path('crear_mascota/', views.create_pet, name='create_pet'),  # Cambiado de crear_mascota a create_pet
    path('mascota/<int:pet_id>/detalle/', views.pet_detail, name='pet_detail'),  # Cambiado de detalle_mascota a pet_detail
    path('delete_pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    path('increase_hunger/<int:pet_id>/', views.increase_hunger, name='increase_hunger'),
    path('increase_energy/<int:pet_id>/', views.increase_energy, name='increase_energy'),
    path('increase_happiness/<int:pet_id>/', views.increase_happiness, name='increase_happiness'),
    path('image-proxy/<path:image_url>/', views.image_proxy, name='image_proxy'),
]

