from django.db import models

# Create your models here.

#info for session
class Session(models.Model):
    date_of_appointment = models.DateTimeField()

    class Meta:
        db_table = "Session"

    def __str__(self):
        return f"{self.therapist} ({self.date_of_appointment})"