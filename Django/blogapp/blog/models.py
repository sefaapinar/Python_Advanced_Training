from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField(default=False)

    
class Category(models.Model):
    name = models.CharField(max_length=250)


