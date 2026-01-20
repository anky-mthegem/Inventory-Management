from django.contrib import admin

from inventory.models import History_table, Product_table

# Register your models here.
class Product_admin(admin.ModelAdmin):
    
    list_display = ('autoincrementid', 'InvoiceNo',
                    'Description', 'Quantity', 'PO_no', 'ChallanNo', 'Itemcode', 'MatType', 'Order_by', 'Used_by', 'Received_by','Punched_date', 'Location', 'Active', 'Timestamp',)

class History_admin(admin.ModelAdmin):
    
    list_display = ('autoincrementid', 'Hist_invoice', 'Hist_description', 
                    'Hist_quantity', 'Hist_ajdqty', 'Hist_po', 'Hist_MatType', 'Active', 'Timestamp', 'Location', 'Order_by', 'User')

admin.site.register(Product_table, Product_admin)
admin.site.register(History_table, History_admin)