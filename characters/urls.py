from django.urls import path

from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='list'),
    path('personajes/<slug:slug>/', views.CharacterDetailView.as_view(), name='detail'),
]
