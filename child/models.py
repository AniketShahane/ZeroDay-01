from django.db import models
from django.utils import timezone
# Create your models here.
class Child(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=150)
    grades = models.TextField()
    ambition = models.TextField()
    joined = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name