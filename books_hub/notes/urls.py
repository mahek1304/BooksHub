from django.contrib import admin
from . import views
from django.urls import path,include
from django.views.generic.base import TemplateView

app_name='notes'

urlpatterns = [
    path('notes_list/', views.NotesListView.as_view(), name='list'),
]