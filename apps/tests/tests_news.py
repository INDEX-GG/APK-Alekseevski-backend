import tempfile
from datetime import date
from PIL import Image
from pytils.translit import slugify
from rest_framework import status
from rest_framework.test import APITestCase
from apps.news.models import News


class NewsTests(APITestCase):
    def test_create_news(self):
        url = '/api/v1/news/'
        data = {'title': 'Новость',
                'description': 'Описание',
                'text': 'Текст',
                'image': temporary_image(),
                'publish': True}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.get().title, 'Новость')
        self.assertEqual(News.objects.get().slug, slugify(News.objects.get().title))
        self.assertEqual(News.objects.get().description, 'Описание')
        self.assertEqual(News.objects.get().text, 'Текст')
        self.assertEqual(News.objects.get().date, date.today())
        self.assertEqual(News.objects.get().publish, True)

    def test_list_news(self):
        url = '/api/v1/news/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


def temporary_image():
    """ Returns a new temporary image file """
    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_file, 'jpeg')
    tmp_file.seek(0)
    return tmp_file
