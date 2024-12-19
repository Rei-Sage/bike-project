# Generated by Django 5.1.3 on 2024-11-25 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0006_categorybike_bike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorybike',
            name='bike',
        ),
        migrations.AlterField(
            model_name='categorybike',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_product', to='bike.bike', verbose_name='Категория'),
        ),
    ]