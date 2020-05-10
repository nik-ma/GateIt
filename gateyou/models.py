from django.db import models

# Create your models here.
class viewers(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.IntegerField(default=1)

