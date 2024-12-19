from django.db import models

# Create your models here.
from django.utils import timezone
from django.db import models
from django.utils.text import slugify

from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.conf import settings

# from account.models import User
    
class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField('название', max_length=250, unique=True)
    
    def __str__(self):
        return f'{self.name}'

class Size(models.Model):
    class Meta:
        verbose_name = 'размер'
        verbose_name_plural = 'размеры'

    name = models.CharField('название', max_length=255)

    def __str__(self):
        return f'{self.name}'
class Brand(models.Model):
    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'

    name = models.CharField('название', max_length=255)

    def __str__(self):
        return f'{self.name}'
    
class FrameMaterial(models.Model):
    class Meta:
        verbose_name = 'Материал рам'
        verbose_name_plural = 'Материал рамы'
    
    name = models.CharField('название', max_length=255)

    def __str__(self):
        return f'{self.name}'
    
class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цветы'
        
    name = models.CharField('цвет', max_length=20)
    image = models.ImageField('color', upload_to='images/')
    def __str__(self):
        return f'{self.name}'

class Flag(models.Model):
    class Meta:
        verbose_name = 'Флаг'
        verbose_name_plural = 'Флаги'
        
    name = models.CharField('Флаг', max_length=100)
    image = models.ImageField('флаг', upload_to='images/')
    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    ORDER_STATUS = (
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    )
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')  
    bike = models.ForeignKey('bike.Bike', on_delete=models.CASCADE, verbose_name='велосипед')
    quantity = models.PositiveIntegerField('количество', default=1)
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    status = models.CharField('статус заказа', max_length=20, choices=ORDER_STATUS, default=PENDING)
    order_date = models.DateTimeField('дата заказа', auto_now_add=True)

    def __str__(self):
        # return f'Order #{self.id} by {self.user} for {self.bike.name}'
        return f'Order #{self.id} by for {self.bike.name}'

    @property
    def total_price(self):
        return self.quantity * self.price

# class Wishlist(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
#     bike = models.ForeignKey('bike.Bike', on_delete=models.CASCADE, verbose_name="Велосипед")
#     added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата доб")

#     class Meta:
#         unique_together = ('user', 'bike')
#         verbose_name = "Список желаний"
#         verbose_name_plural = "Списки желаний"

#     def __str__(self):
#         return f'{self.user.username} - {self.bike.name}'



class CategoryBike(models.Model):
    class Meta:
        verbose_name = 'Малые подкатегории'
        verbose_name_plural = 'Малая подкатегория'
    name = models.CharField(max_length=20, verbose_name='Подкатегория')
    product = models.ForeignKey("Category",related_name='cat_product', verbose_name="Категория", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name


    

class Cart(models.Model):
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"Корзина {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    bike = models.ForeignKey('bike.Bike', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    @property
    def total_price(self):
        return self.price * int(self.quantity) 


class Product_Image(models.Model):
    class Meta:
        verbose_name = 'Фото карточки'
        verbose_name_plural = 'Фото карточек'
        
    image = models.ImageField(upload_to="many_image", verbose_name="Фото")
    product = models.ForeignKey("Bike",related_name='anime', verbose_name="Продукт", on_delete=models.CASCADE)




IN_STOCK = 'В наличии'
SOLD_OUT = 'Распродано'

RECEIVE_TYPE = (
    (IN_STOCK, 'В наличии'),
    (SOLD_OUT, 'Распродано')
)

class Bike(models.Model):
    class Meta:
        verbose_name = 'велосипед'
        verbose_name_plural = 'велосипеды'

    name = models.CharField('название', max_length=100,blank=True)
    created_at = models.DateTimeField('дата добавления', auto_now_add=True)
    updated_at = models.DateTimeField('дата изменения', auto_now=True)

    frame_material = models.ForeignKey('bike.FrameMaterial', on_delete=models.PROTECT, verbose_name='Материал рам', help_text='Выберите материал рамы')
    description = models.CharField('описание', max_length=400, help_text='Краткое описание велосипеда')
    category = models.ForeignKey('bike.Category', on_delete=models.PROTECT, verbose_name='категория', help_text='Выберите категорию')
    brand = models.ForeignKey('bike.Brand', on_delete=models.PROTECT, verbose_name='бренд', help_text='Выберите бренд')
    color = models.ForeignKey('bike.Color', on_delete=models.PROTECT, verbose_name='цвет', help_text='Выберите цвет')
    flag = models.ForeignKey('bike.Flag', on_delete=models.PROTECT, verbose_name='флаг', help_text='Выберите флаг')
    size = models.ForeignKey('bike.Size', on_delete=models.PROTECT, verbose_name='размер', help_text='Выберите размер')

    price = models.DecimalField('цена', max_digits=10, decimal_places=2, default=0.0, validators=[MinValueValidator(0)])
    is_published = models.BooleanField('публичность', default=True)
    receive_type = models.CharField('условия получения', choices=RECEIVE_TYPE, default=IN_STOCK, max_length=15)
    image = models.ImageField('изображение', upload_to='images/')
    year = models.IntegerField('год', validators=[MinValueValidator(1900)])
    wheel_diameter = models.DecimalField('диаметр колеса', max_digits=3, decimal_places=1, default=0.0, validators=[MinValueValidator(0)])
    
    tires = models.CharField('покрышки', max_length=170)
    frame = models.CharField('рамка', max_length=170)
    seatpost = models.CharField('подседельный штырь', max_length=170)
    saddle = models.CharField('седло', max_length=170)
    fork = models.CharField('вилка', max_length=170)
    takeaway = models.CharField('вынос', max_length=170)
    wheels = models.CharField('колеса', max_length=170)
    handlebar = models.CharField('руль', max_length=170)
    brake_system = models.CharField('тормозная система', max_length=170)
    shifters = models.CharField('манетки', max_length=170)
    connecting_rod_system = models.CharField('система шатунов', max_length=170)
    rear_derailleur = models.CharField('задний переключатель', max_length=100)
    chain = models.CharField('цепь', max_length=50)
    num_gears = models.IntegerField('количество передач', validators=[MinValueValidator(1)])
    warranty_years = models.IntegerField('гарантия (годы)', validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name
