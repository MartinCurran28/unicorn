from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField()
    views = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='image')
    
    def __str__(self):
        return self.name + self.description
        
    def __unicode__(self):
        return self.views + self.price