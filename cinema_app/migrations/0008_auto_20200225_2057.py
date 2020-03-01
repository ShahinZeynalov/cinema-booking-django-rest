# Generated by Django 3.0.3 on 2020-02-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0007_auto_20200222_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='age_restriction',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='now_playing',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ticket_id',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]