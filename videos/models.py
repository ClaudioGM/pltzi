from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):

    title = models.CharField(
        max_length=256,
        null=False
    )

    views = models.IntegerField(null=False, default=0)

    author = models.CharField(max_length=200)

    youtube_id = models.CharField(max_length=50, null=False)

    thumbnail_url = models.URLField(max_length=200)

    slug = models.SlugField(max_length=200,unique=True)

    likes = models.ManyToManyField(User)

    dislikes = models.ManyToManyField(
        User,
        related_name='dislike_videos'
    )

    comments = models.ManyToManyField(
        User,
        through='Comment',
        related_name='comments_videos'
    )

    active = models.BooleanField(default=True)
    publicado = models.DateTimeField(
        #auto_now_add=True, Debe ser de esta manera sin embargo,
        #para efectos de la prueba se ha modificado
        null=True,
        blank=True,
    )
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Comment(models.Model):

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.CharField(max_length=300, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VideoViewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='vidsviewed_user')
    video = models.ForeignKey(Video, on_delete=models.CASCADE,
                              related_name='vidsviewed_video')
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-viewed_at',)

    def __str__(self):
        return '{} viewed by {}'.format(self.title, self.author)

    def save(self, *args, **kwargs):
        #if self._state.adding is True:
            # Aca se incluiria logica
            # que verifique un maximo de videosviewed por mes o
            # cantidad por usuario etc. Y elimine lo que no cumpla el
            # o los criterios establecidos
        super(VideoViewed, self).save(*args, **kwargs)
