from rest_framework.serializers import ModelSerializer
from .models import Product, ProductImage, Category, Comment


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductImageSerializer(ModelSerializer):

    class Meta:
        model = ProductImage
        fields = "__all__"


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    comments = CommentSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
