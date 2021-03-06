from django.db import models
from django.db.models import permalink

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=100, unique=True)
  unique_sig = models.SlugField(max_length=100, unique=True)
  body = models.TextField()
  posted = models.DateField(db_index=True, auto_now_add=True)
  category = models.ForeignKey('blog.Category')

  def __str__(self):
    return self.title

  @permalink
  def get_absolute_url(self):
    return ('view_blog_post', None, { 'slug': self.unique_sig })

class Category(models.Model):
  title = models.CharField(max_length=100, db_index=True)
  unique_sig = models.SlugField(max_length=100, db_index=True)

  def __str__(self):
    return self.title

  @permalink
  def get_absolute_url(self):
    return ('view_blog_category', None, { 'slug': self.unique_sig })


