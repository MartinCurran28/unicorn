from django.test import TestCase
from features.models import Debug

class FeaturesTest(TestCase):

 def test_str_name(self):
        test_name = Debug(name = 'Paul McCartney')
        self.assertEqual(str(test_name), 'Paul McCartney')
        
 def test_str_description(self):
        test_description = Debug(description = 'Debug Your Computer For Free!!')
        self.assertEqual(str(test_description), 'Debug Your Computer For Free!!')  
        
 def test_str_views(self):
        test_views = Debug(views = '')
        self.assertEqual(str(test_views), '')  
        
 def test_str_likes(self):
        test_likes = Debug(likes = '')
        self.assertEqual(str(test_likes), '')         
        
         
