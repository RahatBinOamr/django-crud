from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    position = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)


# Create your models here.
