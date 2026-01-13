from rest_framework import serializers
from product.models.product import Product
from order.models.order import Order
from product.serializers.product_serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(many=True, read_only=True)

    
    products_id = serializers.PrimaryKeyRelatedField(
    queryset=Product.objects.all(),
    write_only=True,
    many=True,
    required=False
)

    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['user', 'product', 'products_id', 'total']

    def get_total(self, instance):
        return sum(p.price for p in instance.product.all())

    def create(self, validated_data):
        products = validated_data.pop('products_id')
        user = validated_data.pop('user')

        order = Order.objects.create(user=user)
        order.product.set(products)

        return order
