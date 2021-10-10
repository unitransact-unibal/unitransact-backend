from django.db import models


class Parent(models.Model):
    national_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    user_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.national_id)
