from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits=7, decimal_places=2)    

    def __str__(self):
        return self.name
