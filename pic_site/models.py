# models.pys
from django.db import models

class Images(models.Model):
    img_url = models.TextField()
    img_style = models.IntegerField()
    img_size = models.IntegerField()
    img_color = models.IntegerField()
    img_title = models.CharField(max_length=50,default="image title")
    def __str__(self):
        return self.img_title

class Style(models.Model):
    style_name = models.CharField(max_length=20)
    def __str__(self):
        return self.style_name

class Size(models.Model):
    size_name = models.CharField(max_length=20)
    def __str__(self):
        return self.size_name

class Color(models.Model):
    color_name = models.CharField(max_length=20)
    def __str__(self):
        return self.color_name

