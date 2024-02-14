from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bdev_crowler.crowler.models import DataCollected


class TestCrowler(APITestCase):
    def test_crowl_api_1(self):
        param = 'dog'
        url = reverse('colect-data', kwargs={'search': param})
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DataCollected.objects.count(), 1)
