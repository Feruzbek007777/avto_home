from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    made_year = models.IntegerField(default=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Ustoz haydovchi haqida qoshdim !!!

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name
