# Generated by Django 3.1.7 on 2021-04-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210423_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='mobile',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]