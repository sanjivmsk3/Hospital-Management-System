# Generated by Django 3.2.7 on 2021-09-23 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_paitent_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='paitent',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
