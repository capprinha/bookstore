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
    products_id = serializers.PrimaryKeyRelatedField(
        queyset=Product.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Order
        fields = ['user', 'product', 'total']

    def get_total(self, instance):
        return sum(p.price for p in instance.product.all())
    
    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        user_data = validated_data.pop('user')

        order = Order.objects.create(user = user_data)
        for product in product_data:
            order.product.add(product)

        return order
