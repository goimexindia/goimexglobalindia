# Generated by Django 3.1.7 on 2021-05-03 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_view_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]