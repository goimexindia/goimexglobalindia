# Generated by Django 3.1.7 on 2021-05-15 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyerseller', '0002_order_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['full_name']},
        ),
    ]