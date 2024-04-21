from django.test import TestCase
from .models import Post
# Create your tests here.
import random
import string
from django.urls import reverse
class PostModelTest(TestCase):
    
    def setUp(self):
        #getting random string
        random_text = generate_random_text(4)
        print(random_text)
        self.post = Post.objects.create(text=random_text)

    def test_text_content(self):
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(self.post.text, post.text)

#generates random strings
def generate_random_text(length):
    # Define the characters you want to include in the random text
        characters = string.ascii_letters + string.digits + string.punctuation + ' '

    # Generate random characters to form the text
        random_text = ''.join(random.choice(characters) for _ in range(length))

        return random_text


class HomePageViewTest(TestCase):
    def setUp(self):
          Post.objects.create(text = generate_random_text(4))
    def test_view_url_by_name(self):
         resp = self.client.get(reverse('home'))
         self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):
         resp = self.client.get(reverse('home'))
         self.assertEqual(resp.status_code,200)
         self.assertTemplateUsed(resp,'home.html')


