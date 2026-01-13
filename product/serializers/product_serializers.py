from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(many=True, read_only=True)

    
    categoties_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True,
        source='categoties'
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'category',
            'categoties_id'
        ]

    def create(self, validated_data):

        categories = validated_data.pop('categoties')

        product = Product.objects.create(**validated_data)
        product.category.set(categories)

        return product
