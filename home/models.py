from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)