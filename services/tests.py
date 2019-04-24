from django.test import TestCase
from .models import Service

class ServiceTest(TestCase):
    """
    Here we'll define the tests
    that run against our product models
    """
    
    def test_str(self):
        test_name = Service(name = 'A Service')
        self.assertEqual(str(test_name), 'A Service')
    def test_str_desc(self):
        test_desc = Service(name = 'This service is provided by Bedbug')
        self.assertEqual(str(test_desc), 'This service is provided by Bedbug')
        
    def test_str_price(self):
        test_price = Service(name = '20.00')
        self.assertEqual(str(test_price), '20.00')    
            
    
        

                
