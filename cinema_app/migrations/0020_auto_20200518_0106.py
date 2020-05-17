# Generated by Django 3.0.3 on 2020-05-17 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0019_auto_20200326_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='halls', to='cinema_app.Theater'),
        ),
        migrations.AlterField(
            model_name='session',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='cinema_app.Hall'),
        ),
        migrations.AlterField(
            model_name='theater',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theaters', to='cinema_app.City'),
        ),
    ]
