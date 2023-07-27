from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='post', on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete = models.CASCADE ,related_name='post')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)

    def __str__(self):
        return self.title
        

class Image(models.Model):
    image = models.FileField(upload_to='media')
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    
    # def __str__(self):
    #     return self.image


