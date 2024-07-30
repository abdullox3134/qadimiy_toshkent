# Generated by Django 5.0.6 on 2024-07-30 14:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('archaeology', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='archaeology',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='liked_kanferensiyalar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='archaeologypicture',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archaeologyPicture', to='archaeology.archaeology'),
        ),
        migrations.AddField(
            model_name='items',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='like_kanferensiyalar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemspicture',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_items', to='archaeology.items'),
        ),
        migrations.AddField(
            model_name='itemsvideo',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_items', to='archaeology.items'),
        ),
        migrations.AddField(
            model_name='newspicture',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_picture', to='archaeology.news'),
        ),
    ]
