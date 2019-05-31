from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=300)
    rolln=models.IntegerField()
    admissionn=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    admission_year=models.IntegerField()