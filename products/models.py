from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    rating = models.IntegerField()
    store_name = models.CharField(max_length=255)
    store_url = models.CharField(max_length=255)
    store_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)