from django.db import models
from django.utils import timezone



class Form(models.Model):
    
    name =  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __str__(self):
        return self.name + self.email + self.title + self.content
        
    def __unicode__(self):
        return self.image
        
    