import pytest
from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_category_serializer_valid_data():
    data = {
        'title': 'Auto-ajuda',
        'slug': 'auto-ajuda',
        'description': 'Livros de desenvolvimento pessoal',
        'active': True
    }

    serializer = CategorySerializer(data=data)

    assert serializer.is_valid(), serializer.errors