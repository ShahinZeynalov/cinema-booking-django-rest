# Generated by Django 3.0.3 on 2020-02-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0012_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='format',
        ),
        migrations.AddField(
            model_name='movie',
            name='format',
            field=models.ManyToManyField(to='cinema_app.MovieFormat'),
        ),
    ]
