from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author')
    des = models.TextField()
    profession = models.CharField(max_length=212)
    twitter_link = models.URLField()
    github_link = models.URLField()
    insta_link = models.URLField()
    facebook_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Subscribe(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Advertise(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class InstagramImage(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=212)
    author_name = models.CharField(max_length=212)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    dec = models.TextField()
    quotes = models.TextField()
    extra_images = models.ImageField()
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    image = models.ImageField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

