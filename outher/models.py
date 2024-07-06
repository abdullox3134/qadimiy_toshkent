from django.db import models


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Olimlar(models.Model):
    fullname = models.CharField(max_length=150)
    pasition = models.CharField(max_length=200)
    image = models.FileField(upload_to='image/')


class Kutubxona(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    file = models.FileField(upload_to='images/', blank=True, null=True)
    downloads = models.PositiveIntegerField(default=0, blank=True, null=True)


class Muzeylar(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    link = models.URLField()

    def __str__(self):
        return self.title
