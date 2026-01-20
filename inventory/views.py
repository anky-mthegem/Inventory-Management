from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db.models import Q
import qrcode
from inventory.forms import QRCodeForm
from inventory.models import History_table, Product_table

# Create your views here.

# Login view for site authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == '123456':
            request.session['user_authenticated'] = True
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials. Please try again.'})
    else:
        return render(request, 'login.html')

# Logout view to clear session and redirect to login
def logout_view(request):
    request.session.flush()
    return redirect('login')

def home(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    print("inside home view")
    return render(request, 'matin.html')

def mat_in(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    error_message = None  # Initialize error message
    if request.method == "POST":
        print(request.POST)
        Material_id= request.POST.get("ItemQR").split('/')
        print(Material_id[0])
        Location_id= request.POST.get("LocQR")
        print(Location_id)
        
        print("Length====",len(Material_id))
        print(len(Location_id))
        # Ensure Material_id has at least 10 elements to avoid IndexError
        if len(Material_id) >= 10 and len(Location_id) >=9:
            print("IN view")
            # Get default values for empty fields
            default_punched_date = Material_id[10] if Material_id[10] else datetime.datetime.now().strftime('%Y-%m-%d')
            
            Product_table.objects.create(PO_no= Material_id[0], 
                                         InvoiceNo= Material_id[1], 
                                         ChallanNo= Material_id[2],
                                         Itemcode= Material_id[3],
                                         Description= Material_id[4], 
                                         Quantity= Material_id[5], 
                                         MatType= Material_id[6],
                                         Order_by=Material_id[7],
                                         Received_by= Material_id[8], 
                                         Comments= Material_id[9],
                                         Punched_date= default_punched_date, 
                                         Location=Location_id)
                
            #WB8000400/SDN345/4747489/56101DG4677/PCB Kit/10/Electronics/Siddhesh/Rohit/comments/punched_date YYYY-MM-DD

            print("data entered successfully_!!!!")
            
            History_table.objects.create(Hist_po= Material_id[0], Hist_invoice = Material_id[1], Hist_itemcode=Material_id[3] ,Hist_description= Material_id[4], Hist_quantity= Material_id[5], Hist_MatType= Material_id[6],Order_by=Material_id[7], Location=Location_id)
            
        else:
            error_message = "Error: Invalid length of Material_QR or Location_QR"

    return render(request, 'matin.html', {'error_message': error_message})   

#To display the items in Stock
def mat_out(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    print("inside display view")
    data= Product_table.objects.filter(Active=True).order_by('-Timestamp')
    print(data)
    return render(request,'matout.html', {'items':data}) 

# To display the Details on OUT Page
def out_data(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    PO_no = request.GET.get('PO_no')
    Invoice = request.GET.get('InvoiceNo')
    Description = request.GET.get('Description')
    Quantity = request.GET.get('Quantity')

    missing = []
    if not PO_no:
        missing.append('PO_no')
    if not Invoice:
        missing.append('InvoiceNo')
    if not Description:
        missing.append('Description')
    if not Quantity:
        missing.append('Quantity')

    if missing:
        error_message = f"Missing required parameter(s): {', '.join(missing)}. Please access this page via a valid transfer link."
        return render(request, 'out.html', {
            'error_message': error_message
        })

    return render(request, 'out.html', {
        'PO_no': PO_no,
        'InvoiceNo': Invoice,
        'Description': Description,
        'Quantity': Quantity,
    })

# To adjust the quantity after OUT
def out_qty(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    if request.method == 'POST':
        PO = request.POST.get('pono')
        print(PO)
        invoice = request.POST.get('Item')
        print(invoice)
        description = request.POST.get('description')
        print(description)
        quantity = request.POST.get('avquantity')
        print(quantity)
        adj_qty= request.POST.get("quantity")   
        print("_________",adj_qty)
        user= request.POST.get("user")
    
    
    dataobj= Product_table.objects.get(Q(InvoiceNo= invoice) & Q(PO_no= PO)& Q(Description= description)& Q(Active= True))
    print(dataobj)
    # Storing the original quantity
    org_quantity = dataobj.Quantity
    dataobj.Quantity= int(quantity) - int(adj_qty)
    if dataobj.Quantity == 0:
        dataobj.Active= False
    dataobj.Used_by = user
    dataobj.save()
    
    if int(adj_qty) < int(quantity):
        histobj = History_table.objects.filter(Q(Hist_invoice= invoice) & Q(Hist_po= PO)& Q(Hist_description= description)& Q(Active= True))
        print(histobj) 
        if histobj.exists():
            History_table.objects.create(Hist_invoice=invoice, Hist_description= description, Hist_quantity=quantity, Hist_ajdqty= adj_qty, Hist_po= dataobj.PO_no, Hist_MatType= dataobj.MatType ,Order_by=dataobj.Order_by ,User= user)
            print("History table Entry Created________")
        else:
            print("No Data Found")
    else:
        print("adj_qty is not less than quantity, so no entry created in History_table")
    
    return render(request, 'out.html',{'Og_qty': org_quantity,})

def edit_data(request, InvoiceNo):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    # Retrieve the record from the database
    record = Product_table.objects.get(InvoiceNo=InvoiceNo)
    if request.method == 'POST':
        record.PO_no = request.POST['pono']
        record.ChallanNo = request.POST['challanno']
        record.InvoiceNo = request.POST['invoice']
        record.Itemcode = request.POST['item']
        record.Description = request.POST['desc']
        record.Order_by = request.POST['orderby']
        record.Received_by = request.POST['recby']
        record.Comments = request.POST['comment']
        
         # Parse the Punched_date string into a datetime.date object
        punched_date_str = request.POST['punch']
        record.Punched_date = datetime.strptime(punched_date_str, '%Y-%m-%d').date()
        
        record.save()
        return redirect('matout')
    
    return render(request, 'edit.html', {'record': record})

def item_search(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    data= Product_table.objects.filter(Active=True).order_by('-Timestamp')
    return render(request, 'search.html', {'items':data})  

def trans_hist(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    # We use the filter method on the History_table queryset to filter the entries where the Hist_ajdqty field is greater than or equal to 1 (Hist_ajdqty__gte=1).
    data= History_table.objects.filter(Hist_ajdqty__gte=1).order_by('-Timestamp')   
    return render(request, 'history.html', {'item': data})

def generate_qr_code(request):
    if request.session.get('user_authenticated') != True:
        return redirect('login')
    if request.method == 'POST':
        print("inside generate QR")
        form = QRCodeForm(request.POST)
        print (form)
        if form.is_valid():
            print("inside form qr validation")
            cleaned_data = form.cleaned_data  # Get cleaned form data
            # Concatenate input values with "/"
            data = '/'.join(str(cleaned_data[field]) if cleaned_data[field] else '' for field in cleaned_data)
            # Generate QR code
            qr = qrcode.make(data)
            # Convert QR code image to base64 format
            qr_base64 = qr_to_base64(qr)
            return render(request, 'qrcode.html', {'form': form, 'qr_base64': qr_base64})
    else:
        form = QRCodeForm()
    return render(request, 'qrcode.html', {'form': form})

def qr_to_base64(qr):
    import base64
    from io import BytesIO
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode()
