import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from product.models import Product
from product.models.category import Category

# get
@pytest.mark.django_db
def test_product_viewset_list():

    client = APIClient()
    
    Product.objects.create(
        title = 'Produto 1',
        description = 'poduto_teste',
        price = 10
    )
    Product.objects.create(
        title = 'Produto 2',
        description = 'poduto_teste_2',
        price = 20
    )

    url = reverse('products-list', kwargs={'version': 'v1'})
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['title'] == 'Produto 1'

#post
@pytest.mark.django_db
def test_product_viewset_create():
    client = APIClient()

    category = Category.objects.create(
        title='Livros',
        slug='livros'
    )

    payload = {
        'title': 'Produto Novo',
        'description': 'Produto_criado_via_teste',
        'price': 50,
        'categoties_id': [category.id]
    }

    url = reverse('products-list', kwargs={'version': 'v1'})
    response = client.post(url, payload, format='json')

    assert response.status_code == 201
    assert Product.objects.count() == 1
    assert Product.objects.first().title == 'Produto Novo'