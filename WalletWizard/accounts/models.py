from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   created_at = models.DateTimeField(auto_now_add=True)