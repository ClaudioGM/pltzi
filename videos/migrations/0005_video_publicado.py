# Generated by Django 2.1 on 2020-08-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20180915_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='publicado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
