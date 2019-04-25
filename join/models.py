from django.db import models
from django.utils import timezone



class Join(models.Model):
    
    name = models.CharField(max_length=200, default='')
    surname = models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    cover_letter = models.TextField()
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(null=True)
    cv = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.name