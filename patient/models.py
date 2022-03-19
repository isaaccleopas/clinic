from django.db import models

# Create your models here.

#info for patient
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100)
    

    class Meta:
        db_table = "Patient"

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"
    