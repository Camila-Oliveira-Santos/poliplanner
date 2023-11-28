# Generated by Django 4.2.7 on 2023-11-20 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poliplanner', '0015_remove_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='multiplecats', to='poliplanner.category'),
        ),
    ]
