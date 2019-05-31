from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from .models import student
from weasyprint import HTML
import csv
from reportlab.pdfgen import canvas 

def index(request):  
    template = loader.get_template('index.html') # getting our template  
    name=student.objects.order_by('admission_year')
    name1 ={
        'name' : name,
    }
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2017)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2018)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2019)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2001)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2002)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2004)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2017)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2016)
    #name=student.objects.create(name='manav',rolln=1212,admissionn='2018bit',email='xyz@gmail.com',admission_year=2015)
    return HttpResponse(template.render(name1))    

def excel(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    name=student.objects.order_by('admission_year')
    for i in name:
        writer.writerow([i.name,i.rolln,i.admissionn,i.email,i.admission_year])    
    return response 

def pdf(request):
    name=student.objects.order_by('admission_year')
    name1 ={
        'name' : name,
    }
    html_string = render_to_string('index.html', name1)
    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')
    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response

