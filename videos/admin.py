from django.contrib import admin

from .models import Video, Comment

# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', "publicado",)


admin.site.register(Comment) #Agregado a efectos de la prueba
