from django.db import models

# Create your models here.
class Person(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=500)