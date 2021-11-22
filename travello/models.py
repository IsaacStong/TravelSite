from django.db import models


# Create your models here.
'''class Destinations:
    id: int
    name: str
    img: str
    description: str
    price: str
    offer: bool
'''


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pcs')
    desc = models.TextField()
    price = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)
