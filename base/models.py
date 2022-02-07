from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    target_number = models.IntegerField()
    pin = models.IntegerField()

    def __str__(self):
        return f'Cliente: {self.name} #Targeta: {self.target_number}'