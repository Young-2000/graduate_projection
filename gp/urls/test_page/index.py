from django.urls import path
from gp.views.test_page.getinfo import getinfo

urlpatterns = [
    path("getinfo/", getinfo, name="test_page.getinfo"),
]
