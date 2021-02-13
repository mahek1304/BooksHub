from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    branch = models.CharField(max_length = 50)
    year = models.CharField(max_length = 2)
    subject = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)
    files = models.FileField(upload_to='pdfs', null=True)

    def str(self) :
        return self.name

    class Meta :
        ordering = ('year', )
        verbose_name = 'Notes'
        verbose_name_plural = 'Notes'
