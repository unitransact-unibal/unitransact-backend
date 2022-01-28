from django.contrib import admin

from .models import Student, StudentParent, StudentWalletTransaction

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentParent)
admin.site.register(StudentWalletTransaction)
