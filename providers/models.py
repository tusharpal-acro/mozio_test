from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField("name", max_length=250)
    email = models.EmailField()
    phone_number = models.IntegerField("phone")
    language = models.CharField("language", max_length=250)
    currency = models.CharField("currency", max_length=10)
