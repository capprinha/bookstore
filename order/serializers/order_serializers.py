from rest_framework import serializers
from product.models.product import Product
from order.models.order import Order

from product.serializers.product_serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True
    )
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['user', 'product', 'total']

    def get_total(self, instance):
        return sum(p.price for p in instance.product.all())
