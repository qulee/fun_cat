from django.conf import settings

#多条件查询
def getKwargs(data={}):
    kwargs = {}
    for (k, v) in data.items():
        if v != '0':
            kwargs[k] = v
    # 缩进很重要 0.0....
    return kwargs

# from django doc
def handle_uploaded_file(f):
    # image upload path
    img_url = "pic_site/images/upload/" + f.name
    full_url = "statics/" + img_url
    with open(full_url, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return settings.STATIC_URL + img_url
