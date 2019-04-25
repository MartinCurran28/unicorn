from django.test import TestCase
from accounts.models import Post

class PostTest(TestCase):

 def test_str_title(self):
        test_title = Post(title = 'A Review')
        self.assertEqual(str(test_title), 'A Review')
        
 def test_str_content(self):
        test_content = Post(content = 'This is what is wrong...')
        self.assertEqual(str(test_content), 'This is what is wrong...')        
        
        