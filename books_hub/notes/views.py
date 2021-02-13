from django.shortcuts import render
from django.views.generic import ListView
from .models import Notes
from .filters import NotesFilter
# Create your views here.

class NotesListView(ListView) :
    model = Notes
    template_name = 'notes/list.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['filter'] = NotesFilter(self.request.GET, queryset = self.get_queryset())
        return context