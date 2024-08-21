from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order, Specimen, SourceDescription, Patient, Location, OtherDetails, Record
from .serializers import OrderSerializer, SpecimenSerializer, SourceDescriptionSerializer, PatientSerializer, LocationSerializer, OtherDetailsSerializer, RecordSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 

class SpecimenViewSet(viewsets.ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer
    permission_classes = [IsAuthenticated]     

class SourceDescriptionViewSet(viewsets.ModelViewSet):
    queryset = SourceDescription.objects.all()
    serializer_class = SourceDescriptionSerializer
    permission_classes = [IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]   

class OtherDetailsViewSet(viewsets.ModelViewSet):
    queryset = OtherDetails.objects.all()
    serializer_class = OtherDetailsSerializer
    permission_classes = [IsAuthenticated]     

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]     