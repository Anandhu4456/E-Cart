from django.db import models
from django.contrib.auth.models import User

# Model for Customers

class Customer(models.Model):
    LIVE=0
    DELETE=1
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    delete_status = models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.user.username