from django.contrib.auth import get_user_model
from django.db import models

from parents.models import Parent
from schools.models import School


class Student(models.Model):
    admission_number = models.CharField(max_length=50)
    school_id = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    telephone = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    school_id = models.ForeignKey(School, on_delete=models.PROTECT)
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('school_id', 'admission_number')

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


class StudentWalletTransaction(models.Model):
    DEBIT = 'db'
    CREDIT = 'cr'
    TYPE_CHOICES = [
        (DEBIT, 'debit'),
        (CREDIT, 'credit'),
    ]
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=DEBIT
    )

    # from any user
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    # to any student
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students_wallet_transactions'
