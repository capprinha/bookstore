from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    categoties_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True,
        source='categories'
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'categories',
            'categoties_id',
        ]

    def create(self, validated_data):
        categories = validated_data.pop('categories')

        product = Product.objects.create(**validated_data)
        product.categories.set(categories)

        return product
