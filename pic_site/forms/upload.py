from django import forms
from pic_site.models import *

STYLE_CATEGORY = Style.objects.all()
SIZE_CATEGORY = Size.objects.all()
COLOR_CATEGORY = Color.objects.all()

class UploadImgForm(forms.Form):
    title = forms.CharField(max_length=50, label='标题')
    file = forms.FileField(label='文件')
    style = forms.ModelChoiceField(queryset=STYLE_CATEGORY, empty_label='请选择', label='风格')
    size = forms.ModelChoiceField(queryset=SIZE_CATEGORY, empty_label='请选择', label='尺寸')
    color = forms.ModelChoiceField(queryset=COLOR_CATEGORY, empty_label='请选择', label='颜色')
