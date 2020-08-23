from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    blog_head = models.CharField(max_length=200)
    blog_content = models.CharField(max_length =1000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.blog_head

class Comment(models.Model):
    comment_text = models.ForeignKey(Blog,on_delete= models.CASCADE)
    put_comment = models.CharField(max_length=200)
    co_date = models.DateTimeField('date published')
    def __str__(self):
        return self.put_comment
        '''
#<a href="{% url 'blog:comment' com.id %}">+Comment</a>
'''
