from rest_framework import status
from rest_framework.test import APITestCase
import tempfile
from PIL import Image
from apps.news.models import News


def temporary_image():
    """ Returns a new temporary image file """
    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_file, 'jpeg')
    tmp_file.seek(0)
    return tmp_file


class NewsTests(APITestCase):
    def test_create_news(self):
        url = '/api/v1/news/'
        data = {'title': 'Новостьqwe',
                'description': 'Описание',
                'text': 'Текст',
                'image': temporary_image(),
                'publish': True}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(News.objects.count(), 1)
        # self.assertEqual(News.objects.get().title, 'Новость')
