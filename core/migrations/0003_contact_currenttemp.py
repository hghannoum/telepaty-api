# Generated by Django 3.2.6 on 2023-09-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230921_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='currentTemp',
            field=models.IntegerField(default=0, verbose_name=0),
            preserve_default=False,
        ),
    ]
