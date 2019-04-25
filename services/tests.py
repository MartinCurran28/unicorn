from django.test import TestCase
from services.models import Service

class ServiceTest(TestCase):
    """
    Here we'll define the tests
    that run against our product models
    """
    
    def test_str(self):
        test_name = Service(name = 'A Service')
        self.assertEqual(str(test_name), 'A Service')
        
    def test_str_description(self):
        test_description = Service(description = 'This service is provided by Bedbug')
        self.assertEqual(str(test_description), 'This service is provided by Bedbug')
    
    def test_str_views(self):
        test_views = Service(views = "")
        self.assertEqual(str(test_views), "")    
        
    def test_str_likes(self):
        test_likes = Service(likes = "")
        self.assertEqual(str(test_likes), "")       
        
    def test_str_price(self):
        test_price = Service(price = "")
        self.assertEqual(str(test_price), "")      
        
        
        
        
        