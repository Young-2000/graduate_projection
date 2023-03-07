from django.http import JsonResponse

def getinfo(request):
    img_src_yes = "static/images/test_page/yes.png"
    img_src_no = "static/images/test_page/no.png"

    return JsonResponse({
        'result': "success",
        'val_return': img_src_no,
        })
