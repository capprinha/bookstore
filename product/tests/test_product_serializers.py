import pytest
from product.serializers.product_serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer_valid_data():
    data = {
        'title' : 'As 48 leis do Poder',
        'description': 'O poder é um jogo...',
        'price': '79.00',
        'active': True,
        'category': [
            {
                'title': 'Auto-ajuda',
                'slug': 'auto-ajuda'
            }
        ]
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), serializer.errors