# Generated by Django 3.0.3 on 2020-02-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0010_comment_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_restriction',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
