from django.db import models

# Create your models here.
class Users (models.Model) :
    fullname = models.CharField(max_length =200)
    username = models.CharField(max_length =200)
    email = models.EmailField
    Password = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    yearofbirth = models.DateField(null=True)

    def __str__(self):
         return self.fullname


class Product(models.Model):
        product_name = models.CharField(max_length=200)
        product_price = models.CharField(max_length=100)
        product_quantity = models.IntegerField()

        def __str__(self):
            return self.product_name
