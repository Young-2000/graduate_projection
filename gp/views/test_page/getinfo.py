from django.http import JsonResponse
from gp.views.deep_learning_models.prediction import text_prediction

def getinfo(request):
    img_src_yes = "static/images/test_page/yes.png"
    img_src_no = "static/images/test_page/no.png"

    text = request.GET.get("text")
    bully_result = text_prediction(text)

    print(bully_result)

    if bully_result == 1:
        img_src = img_src_yes
    else:
        img_src = img_src_no

    return JsonResponse({
        'result': "success",
        'val_return': img_src,
        })
