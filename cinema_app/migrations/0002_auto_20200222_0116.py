# Generated by Django 3.0.3 on 2020-02-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='casts',
        ),
        migrations.AddField(
            model_name='movie',
            name='casts',
            field=models.CharField(default='Anonyms', max_length=127),
        ),
        migrations.DeleteModel(
            name='Cast',
        ),
    ]
