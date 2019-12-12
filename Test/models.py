
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=254, blank=True, null=True)
    surname = models.CharField(max_length=254, blank=True, null=True)
    login = models.CharField(unique=True, max_length=254, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.login


class Product(models.Model):
    title = models.CharField(max_length=254, blank=False, null=False)
    description = models.CharField(max_length=254, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return '%s %s' % (self.client, self.product)
