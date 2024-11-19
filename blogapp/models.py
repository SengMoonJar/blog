from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image= models.ImageField(default='default.png',blank=True,upload_to='images/')
    author= models.ForeignKey(User,on_delete=models.CASCADE,default=None)

def __str__(self):
    return self.title
def show_article(self):
    return self.body[:50] + '...'