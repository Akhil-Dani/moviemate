from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies, name='index'),
    path('<int:id>/', views.detail)
]
