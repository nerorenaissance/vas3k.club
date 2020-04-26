# Generated by Django 3.0.4 on 2020-04-26 08:23

from django.db import migrations


def backfill_published_date(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    for post in Post.objects.filter(is_visible=True):
        post.published_at = post.created_at
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200425_2028'),
    ]

    operations = [
        migrations.RunPython(backfill_published_date),
    ]