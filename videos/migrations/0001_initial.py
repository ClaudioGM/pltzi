# Generated by Django 2.1 on 2018-09-15 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('views', models.IntegerField(default=0)),
                ('author', models.CharField(max_length=200)),
                ('youtube_id', models.CharField(max_length=50)),
                ('thumbnail_url', models.URLField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('comments', models.ManyToManyField(related_name='comments_videos', through='videos.Comment', to=settings.AUTH_USER_MODEL)),
                ('dislikes_to', models.ManyToManyField(related_name='dislike_videos', to=settings.AUTH_USER_MODEL)),
                ('likes_to', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
    ]
