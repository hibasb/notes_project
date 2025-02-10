from django.urls import path
from .views import note_list, add_note

urlpatterns = [
    path('', note_list, name='note_list'),
    path('add/', add_note, name='add_note'),
]
