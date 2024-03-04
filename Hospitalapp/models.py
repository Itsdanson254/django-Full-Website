from django.db import models


# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
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


class Member(models.Model):
    Username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username


class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.fullname


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)