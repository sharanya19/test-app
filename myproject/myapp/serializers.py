from rest_framework import serializers
from .models import Order, Specimen, SourceDescription, Patient, Location, OtherDetails,Record

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # You can also list specific fields like ['order_code', 'order_name', ...]


class SpecimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specimen
        fields = ['specimen_id', 'specimen_type', 'specimen_type_snomed_code']

class SourceDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceDescription
        fields = ['source_description', 'specimen_source', 'source_snomed_code']        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['patient_id', 'first_name', 'middle_name', 'last_name',
            'gender', 'dob', 'address_line1', 'address_line2', 'city',
            'state', 'zip', 'email', 'phone_number', 'race', 'ethnicity'
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_id', 'district', 'test_location']

class OtherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDetails
        fields = ['entry_id', 'env', 'extract_flag']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'        