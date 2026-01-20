
from django import views
from django.urls import path
from django.contrib import admin
from inventory.views import edit_data, generate_qr_code, item_search, mat_in, home, mat_out, out_data, out_qty, trans_hist
from inventory.views import login_view
from inventory.views import logout_view

urlpatterns = [
    
    # path('', members, name='members'),
    path('', home, name='home'),
    path('rec/', mat_in, name='hdlin'),
    path('rel/', mat_out, name='matout'),
    path('search/', item_search, name='itemsearch'),
    path('out/', out_data, name='out_data'),
    path('out_qty/', out_qty, name= 'out_qty'),
    path('edit/<str:InvoiceNo>/', edit_data, name= 'edit'),
    path('qrcode/', generate_qr_code, name= 'qrcode'),
    path('hist/',trans_hist, name='transhist'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    
    
    
]