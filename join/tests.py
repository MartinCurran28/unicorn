from django.test import TestCase
from join.models import Join

class JoinTest(TestCase):
    
    def test_str(self):
        test_name = Join(name = 'John')
        self.assertEqual(str(test_name), 'John')
        
    def test_str_surname(self):
        test_surname = Join(surname = 'Lennon')
        self.assertEqual(str(test_surname), 'Lennon')    
        
    def test_str_email(self):
        test_email = Join(email = 'JLeno98@gmail.com')
        self.assertEqual(str(test_email), 'JLeno98@gmail.com')    
    
    def test_str_phone(self):
        test_phone = Join(phone = '0872435463')
        self.assertEqual(str(test_phone), '0872435463')       
        
    def test_str_cover_letter(self):
        test_cover_letter = Join(cover_letter = 'I am hard-working, dedicated, and I havve been told that I am persistent')
        self.assertEqual(str(test_cover_letter), 'I am hard-working, dedicated, and I havve been told that I am persistent')   
        
    def test_str_country(self):
        test_country = Join(country = 'Ireland')
        self.assertEqual(str(test_country), 'Ireland')       
        
    def test_str_postcode(self):
        test_postcode = Join(postcode = 'LS18 4AA')
        self.assertEqual(str(test_postcode), 'LS18 4AA')    
        
    def test_str_town(self):
        test_town = Join(town = 'Clonmel')
        self.assertEqual(str(test_town), 'Clonmel') 
        
    def test_str_street_address1(self):
        test_street_address1 = Join(street_address1 = '19 Rosewood')
        self.assertEqual(str(test_street_address1), '19 Rosewood')
        
    def test_str_street_address2(self):
        test_street_address2 = Join(street_address2 = 'ModelCity Road')
        self.assertEqual(str(test_street_address2), 'ModelCity Road') 
        
    def test_str_county(self):
        test_county = Join(country = 'Clare')
        self.assertEqual(str(test_county), 'Clare') 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
