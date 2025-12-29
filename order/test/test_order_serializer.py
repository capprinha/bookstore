import pytest
from django.contrib.auth.models import User
from product.models.category import Category
from product.models.product import Product
from order.serializers.order_serializers import OrderSerializer

@pytest.mark.django_db
def test_order_serializer_is_valid_data():
    user = User.objects.create_user(
        username="capprinha",
        password="123456"
    )

    category = Category.objects.create(
        title="Auto-ajuda",
        slug="auto-ajuda"
    )

    product = Product.objects.create(
        title="As 48 leis do Poder",
        description="O poder é um jogo...",
        price=79.00,
        active=True
    )
    product.categories.add(category)

    data = {
        "user": user.id,
        "product": [product.id]
    }

    serializer = OrderSerializer(data=data)

    assert serializer.is_valid(), serializer.errors
