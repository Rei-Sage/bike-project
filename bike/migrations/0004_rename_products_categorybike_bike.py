# Generated by Django 5.1.3 on 2024-11-25 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0003_alter_categorybike_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorybike',
            old_name='products',
            new_name='bike',
        ),
    ]
