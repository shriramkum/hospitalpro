from django.contrib import admin
from .models import Doctor ,Patients

class Doctoradmin(admin.ModelAdmin):
    list_display = ['id','Name_doctor','type_doctor','qualification','time','hospital']

admin.site.register(Doctor,Doctoradmin)

class Patientadmin(admin.ModelAdmin):
    list_display = ['doctor','patient_name','disease','contact','adress','relation_patient']

admin.site.register(Patients,Patientadmin)