from rest_framework import status
from rest_framework.test import APITestCase
from apps.profile.models import Profile
import tempfile
from PIL import Image


class ProfileTests(APITestCase):

    def test_create_news(self):
        url = ''
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

