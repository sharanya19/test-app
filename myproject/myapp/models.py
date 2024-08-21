from django.db import models

class Order(models.Model):
    order_code = models.CharField(max_length=100, unique=True)  # OrderCode1, etc.
    order_name = models.CharField(max_length=255)
    order_loinc_code = models.CharField(max_length=100)
    loinc_name = models.CharField(max_length=255)
    order_loinc_description = models.TextField()

    def __str__(self):
        return f"{self.order_code} - {self.order_name}"


class Specimen(models.Model):
    specimen_id = models.CharField(max_length=100, unique=True)
    specimen_type = models.CharField(max_length=255)
    specimen_type_snomed_code = models.CharField(max_length=100)

    def __str__(self):
        return self.specimen_id
    
class SourceDescription(models.Model):
    source_description = models.CharField(max_length=255)
    specimen_source = models.CharField(max_length=255)
    source_snomed_code = models.CharField(max_length=255)

    def __str__(self):
        return self.specimen_source    
    
class Patient(models.Model):
    patient_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    race = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Location(models.Model):
    location_id = models.CharField(max_length=255, unique=True)
    district = models.CharField(max_length=255)
    test_location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.test_location}, {self.district}"    
    
class OtherDetails(models.Model):
    entry_id = models.CharField(max_length=255, unique=True)
    env = models.CharField(max_length=255)
    extract_flag = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.entry_id} - {self.env}"    
    

class Record(models.Model):
    order_code = models.CharField(max_length=100)
    order_name = models.CharField(max_length=100)
    order_loinc_code = models.CharField(max_length=100)
    loinc_name = models.CharField(max_length=100)
    order_loinc_description = models.TextField()
    specimen_id = models.CharField(max_length=100)
    specimen_type = models.CharField(max_length=100)
    specimen_type_snomed_code = models.CharField(max_length=100)
    source_description = models.TextField()
    specimen_source = models.CharField(max_length=100)
    source_snomed_code = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=100)
    patient_first_name = models.CharField(max_length=100)
    patient_middle_name = models.CharField(max_length=100)
    patient_last_name = models.CharField(max_length=100)
    patient_gender = models.CharField(max_length=10)
    dob = models.DateField()
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    race = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)
    entry = models.CharField(max_length=100)
    env = models.CharField(max_length=100)
    extract_flag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.order_code} - {self.order_name}"