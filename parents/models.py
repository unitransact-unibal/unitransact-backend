from django.db import models
from django.contrib.auth import get_user_model


class Parent(models.Model):
    national_id = models.CharField(max_length=50, unique=True)
    telephone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.national_id)
