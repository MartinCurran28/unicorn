from django.db import models

class Debug(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.name
        
class Future_Feature(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image')
    
    
    def __str__(self):
        return self.name        
        
        