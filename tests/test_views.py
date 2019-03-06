from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from blog.views import PostListView
from django.urls import reverse


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_post = 3
        user = User.objects.create_user(username='Ivanov')
        for post_num in range(number_of_post):
            Post.objects.create(author=user, title=f'Тестирование поста {post_num}', text=f'Описание тестового поста{post_num}')

    def test_list_view_urls(self):
        resp = self.client.get(reverse('posts'))
        self.assertEqual(resp.status_code, 200)

    def test_detail_view_urls(self):
        resp = self.client.get(reverse('post_detail', args=['1']))
        self.assertEqual(resp.status_code, 200)

    def test_edit_view_urls(self):
        resp = self.client.get(reverse('post_edit', args=['1']))
        self.assertEqual(resp.status_code, 200)

    def test_create_view_urls(self):
        resp = self.client.get(reverse('post_new'))
        self.assertEqual(resp.status_code, 200)


class ListViewsTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     user = User.objects.create_user(username='Ivanov')
    #     post1 = Post.objects.create(author=user, title=f'Тестирование поста 1',
    #                                 text=f'Описание тестового поста 1')
    #     post2 = Post.objects.create(author=user, title=f'Тестирование поста 2',
    #                                 text=f'Описание тестового поста 2')
    #     post1.publish()
    #     post2.publish()
    #     post_list = [post1, post2]

    def test_publish(self):

        user = User.objects.create_user(username='Ivanov')
        post1 = Post.objects.create(author=user, title=f'Тестирование поста 1',
                                    text=f'Описание тестового поста 1')
        post2 = Post.objects.create(author=user, title=f'Тестирование поста 2',
                                    text=f'Описание тестового поста 2')
        post1.publish()
        post2.publish()

        self.assertEqual(list(PostListView.get_queryset([post1, post2])), [post2, post1])


