# 只会在web段被调用
from django.shortcuts import render # 渲染html

def index(request):
    return render(request, "test_page/web.html")
