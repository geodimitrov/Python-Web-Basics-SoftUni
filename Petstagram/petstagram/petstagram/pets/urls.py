from django.urls import path

from petstagram.pets.views import pet_all, pet_details, like_pet, create_pet, edit_pet, delete_pet

urlpatterns = [
    path('', pet_all, name="all pets"),
    path('details/<int:pk>', pet_details, name="pet details"),
    path('like/<int:pk>', like_pet, name="like pet"),
    path('create/', create_pet, name="create pet"),
    path('edit/<int:pk>', edit_pet, name="edit pet"),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
]