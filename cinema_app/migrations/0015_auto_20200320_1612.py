# Generated by Django 3.0.3 on 2020-03-20 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0014_auto_20200320_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.City'),
        ),
    ]
