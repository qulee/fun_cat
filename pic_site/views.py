from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pic_site import models
from pic_site.utils import common
from pic_site.forms.upload import UploadImgForm

# index page
def index(request):
    img_style = models.Style.objects.all()
    img_size = models.Size.objects.all()
    img_color = models.Color.objects.all()
    img_url = models.Images.objects.all()
    return render(request, 'pic_site/xiquIndex.html',{
        'img_style':img_style,
        'img_size':img_size,
        'img_color':img_color,
        'img_url':img_url,
    })

# ajax post
@csrf_exempt
def tag_list(request):
    post_data = {}
    if request.method == "POST":
        post_data["img_style"] = request.POST["style_id"]
        post_data["img_size"] = request.POST["size_id"]
        post_data["img_color"] = request.POST["color_id"]
        kwargs = common.getKwargs(post_data)
        res = models.Images.objects.filter(**kwargs)
        json_data = serializers.serialize("json", res)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse("error")

def img_upload(request):
    if request.method == 'POST':
        # bind
        image_dict = {}
        form = UploadImgForm(request.POST, request.FILES)
        if form.is_valid():
            # 存储图片
            img_path = common.handle_uploaded_file(request.FILES['file'])
            # 数据库操作
            image_dict['img_url'] = img_path
            image_dict['img_style'] = form["style"].value()
            image_dict['img_size'] = form["size"].value()
            image_dict['img_color'] = form["color"].value()
            image_dict['img_title'] = form["title"].value()
            img_model = models.Images(**image_dict)
            img_model.save()
            return HttpResponseRedirect('/pic_site/success/')
    else:
        form = UploadImgForm()
    return render(request, "pic_site/upload_page.html", {'form': form})

def success(request):
    return render(request, "pic_site/success.html")
