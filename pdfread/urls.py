from django.urls import path
from . import views

app_name = "pdfread"
urlpatterns =[
    path('index/', views.index, name="index"),
]