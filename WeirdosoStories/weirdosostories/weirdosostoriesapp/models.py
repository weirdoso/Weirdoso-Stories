from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class BookPost(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")  # Images directory
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    wattpad_link = models.CharField(max_length=200, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='book_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)  # Concat purpose: admin side shows title of the blog post, author

    def get_absolute_url(self):  # url to redirect
        return reverse('home')


class Comment(models.Model):
    bookpost = models.ForeignKey(BookPost, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' & (self.bookpost.title, self.name)


class Profile (models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)
    wattpad_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):  # url to redirect
        return reverse('home')


class Subscribers (models.Model):
    emailaddress = models.CharField(max_length=255)

    def __str__(self):
        return str(self.emailaddress)

    def get_absolute_url(self):  # url to redirect
        return reverse('home')
