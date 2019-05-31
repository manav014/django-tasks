from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
from .models import student
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
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    name=student.objects.order_by('admission_year')
    k=0
    for i in name :
        p.drawString(k,0,i.name)  
        #p.drawString(k,10,i.rolln)  
        p.drawString(k,20,i.admissionn)  
        p.drawString(k,30,i.email)  
        #p.drawString(k,40,i.admission_year)  
        
        
    p.showPage()  
    p.save()  
    return response  

