from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

#blogs/1.jpg

class Blog(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="blogs")
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True, editable=False)


    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


#sefapinar.com/category/telefon
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(null=False,unique=True,blank=True, db_index=True, editable=False)

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


    def __str__(self) -> str:
        return self.name


