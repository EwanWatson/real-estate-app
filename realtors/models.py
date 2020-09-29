from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name