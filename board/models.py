from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    article = RichTextField(blank = True, null = True)
    slug = models.SlugField(max_length=200,blank = True, null = True )
    image = models.ImageField(upload_to ='img', blank = True, null = True )
    
    
    def __str__(self):
        return self.title

