from django.http import HttpResponse

def index(request):
    return HttpResponse("网络暴力语言检测")
