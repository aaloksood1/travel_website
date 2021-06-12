from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'travello')
    desc = models.TextField()
    price = models.IntegerField()
    special_offer = models.BooleanField(default = False)

    def update(self, name, image, desc, price, special_offer):
        self.name = name
        self.image = image
        self.desc = desc
        self.price = price
        self.special_offer = special_offer

    def __str__(self):
        return self.name
