import django_filters
from .models import Notes


class NotesFilter(django_filters.FilterSet):

    class Meta :
        model = Notes
        fields = ('branch', 'year', 'subject')