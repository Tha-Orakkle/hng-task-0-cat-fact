from django.urls import reverse
from rest_framework.test import APIClient
import pytest


URL = reverse('data-view')

@pytest.fixture
def client():
    return APIClient()

def test_get_data_view(client):
    res = client.get(URL)
    assert res.status_code == 200
    data = res.json()
    assert data['status'] == 'success'
    assert data['timestamp'] is not None
    assert data['fact'] is not None
    assert data['user'] is not None
    user = data['user']
    assert user['email'] == 'adegbiranayinoluwa.paul@yahoo.com'
    assert user['name'] == 'Paul Adegbiran-Ayinoluwa'
    assert user['stack'] == 'Python/Django'
    
    
def test_rate_limit(client):
    for _ in range(50):
        res = client.get(URL)
        assert res.status_code in (200, 429)
        
    res = client.get(URL)
    assert res.status_code == 429
    data = res.json()
    assert data['error'] == "Too many requests."