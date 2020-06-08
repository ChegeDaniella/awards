from django.test import TestCase
from .models import Posts,Rates
from django.contrib.auth.models import User
# Create your tests here.

class PostTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='testuser',email="email@email.com",password="Test1234")
        self.new_post = Posts(title='Post',image_page="default.png",description="This is a description",link="https://www.github.com",date_posted='june-01-2020',designer=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Posts))

    def tearDown(self):
        Posts.objects.all().delete()
        User.objects.all().delete()

    def test_save_post(self):
        self.new_user.save()
        self.new_post.save_posts()
        post = Posts.objects.all()
        self.assertTrue(len(post)>0)    


    
