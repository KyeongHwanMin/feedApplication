# Generated by Django 4.2.6 on 2023-10-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, null=True, to='post.hashtag'),
        ),
    ]
