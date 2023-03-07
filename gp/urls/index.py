# 将该路径下的其他文件夹的路径include进来
from django.urls import path, include
from gp.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("test_page", include("gp.urls.test_page.index")),
]
