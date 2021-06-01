# Generated by Django 3.1.7 on 2021-04-22 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210422_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.SlugField(default='NONE', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('AGRICULTURE', 'Agriculture'), ('APPAREL', 'Apparel'), ('AUTOMOBILES & MOTORCYCLES', 'Automobiles & Motorcycles'), ('BEAUTY & PERSONAL CARE', 'Beauty & Personal Care'), ('CHEMICALS', 'Chemicals'), ('COMPUTER HARDWARE & SOFTWARE', 'Computer Hardware & Software'), ('CONSTRUCTION & REAL ESTATE', 'Construction & Real Estate'), ('CONSUMER ELECTRONICS', 'Consumer Electronics'), ('ELECTRICAL EQUIPMENT SUPPLIES', 'Electrical Equipment Supplies'), ('ENERGY', 'Energy'), ('ENVIRONMENT', 'Environment'), ('FASHION ACCESSORIES', 'Fashion Accessories'), ('FOOD & BEVERAGE', 'Food & Beverage'), ('FURNITURE', 'Furniture'), ('GIFTS & CRAFTS', 'Gifts & Crafts'), ('HARDWARE', 'Hardware'), ('HEALTH & MEDICAL', 'Health & Medical'), ('HOME & GARDEN', 'Home & Garden'), ('HOME APPLIANCES', 'Home Appliances'), ('INDUSTRIAL PARTS & FABRICATION SERVICES', 'Industrial Parts & Fabrication Services'), ('LIGHTS & LIGHTING', 'Lights & Lighting'), ('LUGGAGE, BAGS & CASES', 'Luggage, Bags & Cases'), ('MACHINERY', 'Machinery'), ('MEASUREMENT & ANALYSIS INSTRUMENTS', 'Measurement & Analysis'), ('MINERALS & METALLURGY', 'Minerals & Metallurgy'), ('MULTIPLE PRODUCTS', 'Multiple Products'), ('OFFICE & SCHOOL SUPPLIES', 'Office & School Supplies'), ('PACKING & PRINTING', 'Packing & Printing'), ('RUBBER & PLASTICS', 'rubber & Plastics'), ('SECURITY & PROTECTION', 'Security & Protection'), ('SERVICE EQUIPMENT', 'Service Equipment'), ('SHOES & FOOTWEAR ACCESSORIES', 'Shoes & Footwear Accessories'), ('SPORTS & ENTERTAINMENT', 'Sports & Entertainment'), ('TELECOMMUNICATION', 'Telecommunication'), ('TEXTILE & LEATHER PRODUCT', 'Textile & Leather Product'), ('TIMEPIECES, JEWELRY , EYEWEAR', 'Timepieces, Jewelry , Eyewear'), ('TOOLS', 'Tools'), ('TOYS & HOBBIES', 'Toys & Hobbies'), ('TRANSPORTATION', 'Transportation')], default='APPAREL', max_length=100),
        ),
    ]