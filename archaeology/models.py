from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()


class Archaeology(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='liked_kanferensiyalar', blank=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Archaeology'
        verbose_name_plural = 'Archaeology'

    def __str__(self):
        return self.title


class ArchaeologyPicture(models.Model):
    image = models.FileField(upload_to='image', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    name = models.ForeignKey(Archaeology, on_delete=models.CASCADE, related_name='archaeologyPicture',
                             blank=True, null=True)


class Items(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(User, related_name='like_kanferensiyalar', blank=True)
    view_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title or ''


class ItemsVideo(models.Model):
    video = models.FileField(upload_to='video', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='video_items')


class ItemsPicture(models.Model):
    image = models.FileField(upload_to='image', blank=True, null=True)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='picture_items')


class News(models.Model):
    title = models.CharField(max_length=60)
    context = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='image', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title or ''


class NewsPicture(models.Model):
    image = models.FileField(upload_to='image', blank=True, null=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_picture', )
