from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='Ivanov')
        Post.objects.create(author=user, title='Тестирование поста', text='Описание тестового поста')

    def test_publish(self):
        post = Post.objects.get(id=1)
        post.publish()
        self.assertTrue(post.published_date, 'Дата не создана')

