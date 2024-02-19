from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=212)
    author = models.CharField(max_length=212)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post')
    description = models.TextField()
    quotes = models.TextField()
    extra_images = models.ImageField(upload_to='posts')
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    image = models.ImageField(upload_to='comments')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Advertise(models.Model):
    image = models.ImageField(upload_to='advert')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)





class Instagram(models.Model):
    image = models.ImageField(upload_to='insta')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image



class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author')
    description = models.TextField()
    profession = models.CharField(max_length=212)
    twitter = models.URLField()
    github = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




