from django.db import models

class InvoiceModel(models.Model):
  CustomerName = models.CharField(max_length=100)
  Date = models.DateField(auto_now_add=True)
  InvoiceID = models.CharField(max_length=100,unique = True)
  

class InvoiceDetailModel(models.Model):
  InvoiceModelID = models.OneToOneField(InvoiceModel, on_delete=models.CASCADE)
  Description = models.CharField(max_length=100)
  Quantity = models.IntegerField()
  UnitPrice = models.FloatField()
  Price = models.FloatField()
