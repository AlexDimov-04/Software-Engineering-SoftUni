from django.test import TestCase
from testing_demos.web.models import Post

class PhoneTest(TestCase):
    VALID_DATA = {
        'title': 'Lost',
        'description': 'Lost again',
        'author_name': 'Test User',
        'author_phone': '+3598888437'
    }

    def test_create_when__valid__expect_to_be_created(self):
        post = Post.objects.create(**self.VALID_DATA)
        self.assertIsNotNone(post.pk)
