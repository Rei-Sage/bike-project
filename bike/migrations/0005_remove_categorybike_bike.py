# Generated by Django 5.1.3 on 2024-11-25 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_rename_products_categorybike_bike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorybike',
            name='bike',
        ),
    ]
