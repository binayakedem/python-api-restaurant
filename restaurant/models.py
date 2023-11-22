from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    
class Food(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

class Table(models.Model):
    number=models.IntegerField()
    is_occupied=models.BooleanField(default=False)
    
class Order(models.Model):
    PENDING_CHOICES='P'
    ACCEPTED_CHOICES='A'
    CANCELLED_CHOICES='C'
    DELIVERED_CHOICES='D'
    STATUS_CHOICES=[
     (PENDING_CHOICES,'Pending'),
     (ACCEPTED_CHOICES,'Accepted'),
     (CANCELLED_CHOICES,'Cancelled'),
     (DELIVERED_CHOICES,'Delivered'),
    ]
    
    
    PAYMENT_STATUS_PENDING_CHOICES='P'
    PAYMENT_STATUS_COMPLETED_CHOICES='C'
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_PENDING_CHOICES,'Completed'),
        (PAYMENT_STATUS_COMPLETED_CHOICES,'Pending'),
    ]
    
    
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,default=PENDING_CHOICES)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING_CHOICES)
    
    
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    status=models.BooleanField(default=False)
    