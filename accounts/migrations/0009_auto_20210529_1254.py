# Generated by Django 3.1.7 on 2021-05-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210529_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img4',
            field=models.ImageField(default='profile2.png', upload_to='pics', verbose_name='Companys/Product Image'),
        ),
    ]
