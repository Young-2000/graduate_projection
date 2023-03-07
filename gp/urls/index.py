from django.urls import path, include
from gp.views.index import index

urlpatterns = [
    path("", index, name="index"),
]
