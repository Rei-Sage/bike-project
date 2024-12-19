# Generated by Django 5.1.3 on 2024-11-25 18:59

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'бренд',
                'verbose_name_plural': 'бренды',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='название')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='цвет')),
                ('image', models.ImageField(upload_to='images/', verbose_name='color')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цветы',
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Флаг')),
                ('image', models.ImageField(upload_to='images/', verbose_name='флаг')),
            ],
            options={
                'verbose_name': 'Флаг',
                'verbose_name_plural': 'Флаги',
            },
        ),
        migrations.CreateModel(
            name='FrameMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'Материал рам',
                'verbose_name_plural': 'Материал рамы',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'размер',
                'verbose_name_plural': 'размеры',
            },
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('description', models.CharField(help_text='Краткое описание велосипеда', max_length=400, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='цена')),
                ('is_published', models.BooleanField(default=True, verbose_name='публичность')),
                ('receive_type', models.CharField(choices=[('В наличии', 'В наличии'), ('Распродано', 'Распродано')], default='В наличии', max_length=15, verbose_name='условия получения')),
                ('image', models.ImageField(upload_to='images/', verbose_name='изображение')),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900)], verbose_name='год')),
                ('wheel_diameter', models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)], verbose_name='диаметр колеса')),
                ('tires', models.CharField(max_length=170, verbose_name='покрышки')),
                ('frame', models.CharField(max_length=170, verbose_name='рамка')),
                ('seatpost', models.CharField(max_length=170, verbose_name='подседельный штырь')),
                ('saddle', models.CharField(max_length=170, verbose_name='седло')),
                ('fork', models.CharField(max_length=170, verbose_name='вилка')),
                ('takeaway', models.CharField(max_length=170, verbose_name='вынос')),
                ('wheels', models.CharField(max_length=170, verbose_name='колеса')),
                ('handlebar', models.CharField(max_length=170, verbose_name='руль')),
                ('brake_system', models.CharField(max_length=170, verbose_name='тормозная система')),
                ('shifters', models.CharField(max_length=170, verbose_name='манетки')),
                ('connecting_rod_system', models.CharField(max_length=170, verbose_name='система шатунов')),
                ('rear_derailleur', models.CharField(max_length=100, verbose_name='задний переключатель')),
                ('chain', models.CharField(max_length=50, verbose_name='цепь')),
                ('num_gears', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='количество передач')),
                ('warranty_years', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='гарантия (годы)')),
                ('brand', models.ForeignKey(help_text='Выберите бренд', on_delete=django.db.models.deletion.PROTECT, to='bike.brand', verbose_name='бренд')),
                ('category', models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.PROTECT, to='bike.category', verbose_name='категория')),
                ('color', models.ForeignKey(help_text='Выберите цвет', on_delete=django.db.models.deletion.PROTECT, to='bike.color', verbose_name='цвет')),
                ('flag', models.ForeignKey(help_text='Выберите флаг', on_delete=django.db.models.deletion.PROTECT, to='bike.flag', verbose_name='флаг')),
                ('frame_material', models.ForeignKey(help_text='Выберите материал рамы', on_delete=django.db.models.deletion.PROTECT, to='bike.framematerial', verbose_name='Материал рам')),
                ('size', models.ForeignKey(help_text='Выберите размер', on_delete=django.db.models.deletion.PROTECT, to='bike.size', verbose_name='размер')),
            ],
            options={
                'verbose_name': 'велосипед',
                'verbose_name_plural': 'велосипеды',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.bike')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bike.cart')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryBike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Подкатегория')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_product', to='bike.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Малые подкатегории',
                'verbose_name_plural': 'Малая подкатегория',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20, verbose_name='статус заказа')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='дата заказа')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.bike', verbose_name='велосипед')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='many_image', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime', to='bike.bike', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Фото карточки',
                'verbose_name_plural': 'Фото карточек',
            },
        ),
    ]
