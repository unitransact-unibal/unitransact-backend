from django.urls import path

from .views import DetailStudent, ListStudent

urlpatterns = [
    path('<int:pk>/', DetailStudent.as_view()),
    path('', ListStudent.as_view())
]
