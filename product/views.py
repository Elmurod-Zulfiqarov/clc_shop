from rest_framework.generics import ListAPIView
from helpers.pagination import CustomPagination

from .models import Product
from .serializers import ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.select_related(
        "category").prefetch_related("comments", "images").all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
