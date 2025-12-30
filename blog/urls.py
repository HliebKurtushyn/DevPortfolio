from django.urls import path

from . import views

urlpatterns = [
    path('posts/create/', views.create_post),
    path('about/', views.about_view)
]
