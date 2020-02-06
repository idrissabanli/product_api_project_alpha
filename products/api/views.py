from rest_framework.viewsets import ModelViewSet
from products.models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer