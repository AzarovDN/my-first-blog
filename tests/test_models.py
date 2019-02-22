from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# User.objects.create_user()
# Post.objects.get()

class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='Ivanov')
        Post.objects.create(author=user, title='Тестирование поста', text='Описание тестового поста')

    def test_publish(self):
        post = Post.objects.get(id=1)
        post.publish()
        self.assertTrue(post.published_date, 'Дата не создана')

    # def setUp(self):
    #     post = Post.objects.get(id=1)
    #     post.save()
    #
    # def test_title_label(self):
    #     post = Post.objects.get(id=1)
    #     field_label = post._meta.get_field('title').verbose_name
    #     self.assertEquals(field_label, 'title')
    #
    # def test_text_label(self):
    #     post = Post.objects.get(id=1)
    #     field_label = post._meta.get_field('text').verbose_name
    #     self.assertEquals(field_label, 'text')
    #
    # def test_title_max_length(self):
    #     post = Post.objects.get(id=1)
    #     max_length = post._meta.get_field('title').max_length
    #     self.assertEquals(max_length, 200)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author=Author.objects.get(id=1)
    #     expected_object_name = '%s, %s' % (author.last_name, author.first_name)
    #     self.assertEquals(expected_object_name,str(author))

