# Generated by Django 5.1.3 on 2024-11-25 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0005_remove_categorybike_bike'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorybike',
            name='bike',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bik', to='bike.bike', verbose_name='Товар'),
            preserve_default=False,
        ),
    ]