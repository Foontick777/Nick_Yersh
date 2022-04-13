from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return (f'{self.firstname}, {self.lastname}, {self.age}')
