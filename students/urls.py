from django.urls import path

from .views import ListStudent

urlpatterns = [
    path('', ListStudent.as_view())
]
