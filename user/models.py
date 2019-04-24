from django.db import models
from django.utils import timezone

class User(models.Model):
    
    about_me = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.about_me