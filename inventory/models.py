from datetime import date
from django.db import models

# Create your models here.
class Product_table(models.Model):
    autoincrementid = models.AutoField(primary_key=True)
    InvoiceNo = models.CharField(max_length= 100, blank=True)
    ChallanNo = models.CharField(max_length= 100, blank=True)
    Itemcode = models.CharField(max_length= 100, blank=True)
    Description = models.CharField(max_length = 150)
    Quantity = models.IntegerField(blank=True)
    PO_no = models.CharField(max_length = 100, default=0)
    MatType = models.CharField(max_length = 100, default=0)
    Active = models.BooleanField(default = True)
    Timestamp = models.DateTimeField(null=True, auto_now_add=True)
    Location = models.CharField(max_length= 100, default='Not Assigned')
    Order_by = models.CharField(max_length= 100, default= "System")
    Used_by = models.CharField(max_length= 100, default= "System")
    Received_by = models.CharField(max_length=100, default="System")
    Comments = models.CharField(max_length=100, blank= True)
    Punched_date = models.DateField(default=date.today)
    
    def __str__(self):
        return str(self.InvoiceNo)

class History_table(models.Model):
    autoincrementid = models.AutoField(primary_key=True)
    Hist_invoice = models.CharField(max_length= 100, blank=True)
    Hist_itemcode = models.CharField(max_length= 100, blank=True)
    Hist_description = models.CharField(max_length = 150)
    Hist_quantity = models.IntegerField(default=0)
    Hist_ajdqty = models.IntegerField(default=0)
    Hist_po = models.CharField(max_length = 100, blank=True)
    Hist_MatType = models.CharField(max_length = 100, blank=True)
    Active = models.BooleanField(default = True)
    Timestamp = models.DateTimeField(null=True, auto_now_add=True)
    Location = models.CharField(max_length= 100, default='Not Assigned')
    Order_by = models.CharField(max_length= 100, default= "System")
    User = models.CharField(max_length= 100, default= "System")
    
    def __str__(self):
        return str(self.Hist_invoice)