from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User
from django.urls import reverse


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_post = 3
        user = User.objects.create_user(username='Ivanov')
        for post_num in range(number_of_post):
            Post.objects.create(author=user, title=f'Тестирование поста {post_num}', text=f'Описание тестового поста{post_num}')

    def test_list_view_url(self):
        resp = self.client.get('//')
        self.assertEqual(resp.status_code, 200)

    def test_list_view_urls(self):
        resp = self.client.get(reverse('posts'))
        self.assertEqual(resp.status_code, 200)

    # def test_detail_view_url(self):
    #     resp = self.client.get('/post/1')
    #     self.assertEqual(resp.status_code, 200)

    def test_detail_view_urls(self):
        resp = self.client.get(reverse('post_detail', args=['1']))
        self.assertEqual(resp.status_code, 200)

    # def test_edit_view_url(self):
    #     resp = self.client.get('/post/1/edit')
    #     self.assertEqual(resp.status_code, 200)

    def test_edit_view_urls(self):
        resp = self.client.get(reverse('post_edit', args=['1']))
        self.assertEqual(resp.status_code, 200)
    #
    # def test_create_view_url(self):
    #     resp = self.client.get('/post/new/')
    #     self.assertEqual(resp.status_code, 200)

    def test_create_view_urls(self):
        resp = self.client.get(reverse('post_new'))
        self.assertEqual(resp.status_code, 200)
