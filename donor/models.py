from django.db import models
from datetime import datetime 
from django.utils import timezone

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='test@test.com')
    area = models.CharField(max_length=250)
    amount = models.IntegerField()
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.email 

class RevenueAdded(models.Model):
    principal_amount = models.IntegerField()
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.principal_amount)

class RevenueSpent(models.Model):
    principal_amount = models.IntegerField()
    resource = models.CharField(choices=(('SCH', 'Scholarships'),('ST', 'Stationery'), ('ACC', 'Accommodation'), ('HC', 'Health Care')), max_length=255)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return str(self.principal_amount)
