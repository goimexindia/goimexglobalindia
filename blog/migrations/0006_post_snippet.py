# Generated by Django 3.1.7 on 2021-04-22 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210422_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='APPAREL', max_length=255),
        ),
    ]