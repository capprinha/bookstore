import pytest
from product.serializers.product_serializers import ProductSerializer
from product.models.category import Category

@pytest.mark.django_db
def test_product_serializer_valid_data():
    category = Category.objects.create(
        title = 'Livros',
        slug = 'livros'
    )
    data = {
        'title' : 'As 48 leis do Poder',
        'description': 'O poder é um jogo...',
        'price': '79.00',
        'active': True,
        'categoties_id': [category.id],
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), serializer.errors