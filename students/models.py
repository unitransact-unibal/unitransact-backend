from django.contrib.auth import get_user_model
from django.db import models

from parents.models import Parent


class Student(models.Model):
    admission_number = models.CharField(max_length=50)
    school_id = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    telephone = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    school_id = models.PositiveIntegerField()
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.school_id, self.admission_number)


class StudentParent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    parent_id = models.ForeignKey(Parent, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student_id', 'parent_id')
        db_table = 'students_parent'
