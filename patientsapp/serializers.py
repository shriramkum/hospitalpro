from rest_framework import serializers
from.models import Doctor,Patients


class Doctorserializers(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=['id','Name_doctor','type_doctor','qualification','time','hospital']



class Patientserializers(serializers.ModelSerializer):
    doctor=Doctorserializers()
    class Meta:
        model=Patients

        fields=['doctor','patient_name','disease','contact','adress','relation_patient']