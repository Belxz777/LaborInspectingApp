from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.tutorial_list), 
    path('<int:user_id>/', views.retrieve_user),
    path('<int:user_id>/delete/', views.delete_user)
]