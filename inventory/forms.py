from django import forms

class QRCodeForm(forms.Form):
    PO_Number = forms.CharField(label='PO Number', required=False) #fields which we required to be empty are kept false
    Invoice = forms.CharField(label='Invoice No')
    Challan_no = forms.CharField(label= 'Challan no',required=False)
    Itemcode = forms.CharField(label= 'Itemcode', required=False)
    Description = forms.CharField(label='Description')
    Quantity = forms.CharField(label='Quantity')
    Material_Type = forms.CharField(label='Material Type')
    Ordered_by = forms.CharField(label='Ordered By')
    Received_by = forms.CharField(label='Received By')
    Comments = forms.CharField(label= "Comments", required=False)
    Punched_date = forms.DateField(widget=forms.DateInput(), required=False)
    
    
    #WB8000224/644678/ABT560/56101FG2344/Conveyor belt/5/Mechanical/Siddhesh/Amey/PO punched/2024-04-12
    