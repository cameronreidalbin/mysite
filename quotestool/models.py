from django.db import models

class Parameter(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    def getQuantity(self):
        return self.quantity
    def __str__(self):
        return self.name + " = " + str(self.quantity)