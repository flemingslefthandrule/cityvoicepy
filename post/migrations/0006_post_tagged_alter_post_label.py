# Generated by Django 5.0.3 on 2024-03-11 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_post_label_alter_post_postid_post_label'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tagged',
            field=models.ManyToManyField(blank=True, related_name='Taggedposts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='label',
            field=models.ManyToManyField(blank=True, related_name='posts_with_label', to='post.label'),
        ),
    ]