from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create_song/', views.create_song, name='create_song'),
]
