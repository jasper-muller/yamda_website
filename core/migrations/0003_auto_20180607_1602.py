# Generated by Django 2.0.6 on 2018-06-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180607_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(null=True, upload_to='static/yamda/img/'),
        ),
    ]