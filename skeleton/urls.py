from django.urls import path
from . import views

app = 'skeleton'

urlpatterns = [
   path("", views.index, name = "index"),
]