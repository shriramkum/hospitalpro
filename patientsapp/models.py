from django.db import models
from django.utils import timezone


Type_of_doctor=(

    ("General Physicians","General Physicians"),
    ("Pediatricians","Pediatricians"),
    ("General Surgeon","General Surgeon"),
    ("Cardiologist","Cardiologist"),
    ("Dentist","Dentist"),
    ("ENT Specialist","ENT Specialist"),
    ("Gynecologist","Gynecologist"),
    ("Dermatologists","Dermatologists"),

)


class Doctor(models.Model):
    id=models.IntegerField(primary_key=True)
    Name_doctor=models.CharField(max_length=200)
    type_doctor=models.CharField(max_length=200,choices=Type_of_doctor)
    qualification=models.CharField(max_length=200)
    time=models.DateTimeField(default=timezone.now)
    hospital=models.CharField(max_length=300)
    def __str__(self):
        return self.Name_doctor
    class Meta:
        verbose_name='Doctor'
        verbose_name_plural='Doctors'
class Patients(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=200)
    disease=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    adress=models.CharField(max_length=500)
    relation_patient=models.CharField(max_length=200)
    class Meta:
        verbose_name='Patients'
        verbose_name_plural='Patients'


