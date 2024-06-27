from django.db import models

# Create your models here.
# contact/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
