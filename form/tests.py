from django.test import TestCase
from form.models import Form

class FormTest(TestCase):
    """
    Here we'll define the tests
    that run against our product models
    """
    
    def test_str(self):
        test_name = Form(name = 'form')
        self.assertEqual(str(test_name), 'form')
        
    def test_str_email(self):
        test_email = Form(email = 'martincurran28@hotmail.com')
        self.assertEqual(str(test_email), 'martincurran28@hotmail.com')
        
    def test_str_title(self):
        test_title = Form(title = 'My Bug')
        self.assertEqual(str(test_title), 'My Bug')   
        
    def test_str_content(self):
        test_content = Form(content = 'This is my issue...')
        self.assertEqual(str(test_content), 'This is my issue...')    
        
    def test_str_image(self):
        test_image = Form(image = '')
        self.assertEqual(str(test_image), '')  
        
        
        
        
        
        
        
