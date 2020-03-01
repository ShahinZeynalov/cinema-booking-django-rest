# Generated by Django 3.0.3 on 2020-02-25 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0009_auto_20200225_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cinema_app.Movie'),
            preserve_default=False,
        ),
    ]