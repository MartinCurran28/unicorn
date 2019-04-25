from django.test import TestCase
from Form.models import Form

class FormTest(TestCase):
    
    def test_str(self):
        test_name = Form(name = 'A Service')
        self.assertEqual(str(test_name), 'A Service')
