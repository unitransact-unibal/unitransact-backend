from django.db import models


class Student(models.Model):
    admission_number = models.CharField(max_length=50)
    school_id = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    telephone = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.school_id, self.admission_number)
