from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Character


class CharacterListView(LoginRequiredMixin, ListView):
    queryset = Character.objects.filter(status=Character.Status.PUBLISHED)
    context_object_name = 'characters'


class CharacterDetailView(LoginRequiredMixin, DetailView):
    queryset = Character.objects.filter(status=Character.Status.PUBLISHED)
    context_object_name = 'character'
