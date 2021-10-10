from django.db import models
from django.contrib.auth import get_user_model


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
