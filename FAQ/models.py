from django.db import models
from helpers.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import User


class FAQ(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    created_at = models.DateTimeField(auto_now=True)


class About(BaseModel):
    title = models.CharField(max_length=128)
    sub_content = models.CharField(max_length=256)
    image = models.ImageField(upload_to="media/about/", null=True, blank=True)

    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)

    facebook = models.CharField(max_length=256)
    telegram = models.CharField(max_length=256)
    intagram = models.CharField(max_length=256)
    youtube = models.CharField(max_length=256)


class ContactUs(BaseModel):
    phone = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    addres = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now=True)
