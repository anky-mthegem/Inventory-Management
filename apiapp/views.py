# api/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
import requests
from apiapp.models import XmlData

@csrf_exempt  # Exempt from CSRF validation for simplicity
def receive_xml(request):
    if request.method == 'POST':
        xml_data = request.POST.get('xml_data')
        xml_data = '''
                    <root>
                    <SomeElement>SomeValue</SomeElement>
                    </root>
                    '''
        response = requests.post('http://localhost:8000/api/receive/',    #receive is reference from url.py
                                 headers={'Content-Type': 'application/xml'},
                                 data=xml_data)
        return render(request, 'submit_xml.html', {'response': response.json()})
    return render(request, 'submit_xml.html')
    