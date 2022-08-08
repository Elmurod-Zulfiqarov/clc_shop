from django.db import models
from helpers.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import User


class Post(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="media/post/", null=True, blank=True)
    sub_content = models.CharField(max_length=512, null=True, blank=True)
    content = RichTextUploadingField()

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    published_at = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)

