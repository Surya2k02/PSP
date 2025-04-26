from django.db import models

class Inventory( models.Model ):
    name = models.CharField( max_length=255 )
    description = models.TextField( blank=True, null=True )
    price = models.DecimalField( max_digits=10, decimal_places=2 )
    stock_qty = models.PositiveIntegerField()
    category = models.CharField( max_length=100 )