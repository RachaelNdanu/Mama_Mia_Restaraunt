from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    description = models.TextField(max_length=1000, default='')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='main')  # ✅ New field
    image_url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name
