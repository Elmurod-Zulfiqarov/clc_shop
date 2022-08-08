from django.db import models
from helpers.models import BaseModel
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import User
from product.models import Product


class Cart(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    price = models.CharField(max_length=64)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product


CASH = "cash"
CARD = "card"

PAYMENT_CHOICE = (
    (CASH, "cash"),
    (CARD, "card"),
)


class Order(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    phone = models.CharField(max_length=32)
    fio = models.CharField(max_length=256)

    province = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    settlement = models.CharField(max_length=64)
    addres = models.CharField(max_length=256)
    workplace_addres = models.CharField(max_length=128)

    extra_field = models.TextField()
    payment_type = models.CharField(choices=PAYMENT_CHOICE, max_length=32)
    agree_rules = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.customer


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.order
