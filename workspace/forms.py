from django import forms
from bike.models import *

# class AniForm(forms.Form):
#     title = forms.CharField(label='Название', max_length=100,
#                              widget=forms.TextInput(attrs={'class':'bg-red shadow-md rounded-lg p-6 mb-6'}))
#     original_title = forms.CharField(label='Оригинальное название', max_length=100,
#                                       widget=forms.TextInput(attrs={'class':'bg-white shadow-md rounded-lg p-6 mb-6'}))
#     poster = forms.ImageField(label="Постер", widget=forms.FileInput(attrs={'class':'bg-white shadow-md rounded-lg p-6 mb-6'}))
#     banner = forms.ImageField(label="Баннер",required=False, widget=forms.FileInput(attrs={'class':'bg-white shadow-md rounded-lg p-6 mb-6'}))
#     description = forms.CharField(label='Описание', max_length=200,
#                                    widget=forms.Textarea(attrs={'class':'bg-white shadow-md rounded-lg p-6 mb-6','rows':8}))
#     genres = forms.ModelMultipleChoiceField(label='Жанры', queryset=Genre.objects.all(),
#                                              widget=forms.CheckboxSelectMultiple())
#     tags = forms.ModelMultipleChoiceField(label='Теги', queryset=Tag.objects.all(),
#                                           widget=forms.CheckboxSelectMultiple())
#     studio = forms.ModelChoiceField(label='Студия', empty_label='Выберите студию', queryset=Studio.objects.all())
#     author = forms.CharField(label='Автор', max_length=100,
#                              widget=forms.TextInput(attrs={'class': 'bg-white shadow-md rounded-lg p-6 mb-6', 'placeholder': 'Имя автора...'}))
#     category = forms.ModelChoiceField(label='Категория', empty_label='Выберите категорию', queryset=Category.objects.all(),
#                                        widget=forms.Select(attrs={'class': 'form-select'}))
#     is_published = forms.BooleanField(label='Публичность',required=False, initial=False, widget=forms.CheckboxInput())
#     status = forms.ChoiceField(label='Статус', required=False,choices=[('ongoing', 'Онгоинг'), ('completed', 'Завершено'), ('announced', 'Анонс')])
#     type = forms.ChoiceField(label='Тип',required=False, choices=[('tv', 'TV'), ('movie', 'Movie'), ('ova', 'OVA')])
#     release_date = forms.DateField(label='Дата выхода', required=False,widget=forms.DateInput(attrs={'type': 'date'}))
#     end_date = forms.DateField(label='Дата завершения', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
#     duration = forms.IntegerField(label='Длительность серии',required=False)
#     total_episodes = forms.IntegerField(label='Количество эпизодов', required=False)
#     rating = forms.DecimalField(label='Рейтинг', max_digits=3, decimal_places=1, required=False)

# class NewsForm(forms.Form):
#     title = forms.CharField(label='Название', max_length=100,
#                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'News 1'}))
#     poster = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(label='Описание', max_length=200,
#                                   widget=forms.Textarea(attrs={'class': 'form-control', 'row': 8}))
#     author = forms.CharField(label='Автор', max_length=100,
#                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrtip...'}))
#     category = forms.ModelChoiceField(label='Категорие', empty_label='Select category', queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={'class': 'form-select'}))
#     is_published = forms.BooleanField(label='Публичность', initial=False, widget=forms.CheckboxInput())
#     tags = forms.ModelMultipleChoiceField(label='Теги', queryset=Tag.objects.all(),
#                                           widget=forms.CheckboxSelectMultiple())
#     genres = forms.ModelMultipleChoiceField(label='Теги', queryset=Genre.objects.all(),
#                                           widget=forms.CheckboxSelectMultiple())


#     original_title = forms.CharField(label='Оригинальное название', max_length=100,
#                                       widget=forms.TextInput(attrs={'class':'bg-white shadow-md rounded-lg p-6 mb-6'}))
  
    
  
    # studio = forms.ModelChoiceField(label='Студия', empty_label='Выберите студию', queryset=Studio.objects.all())
    # author = forms.CharField(label='Автор', max_length=100,
    #                          widget=forms.TextInput(attrs={'class': 'bg-white shadow-md rounded-lg p-6 mb-6', 'placeholder': 'Имя автора...'}))
  
   
    # status = forms.ChoiceField(label='Статус', required=False,choices=[('ongoing', 'Онгоинг'), ('completed', 'Завершено'), ('announced', 'Анонс')])
    # type = forms.ChoiceField(label='Тип',required=False, choices=[('tv', 'TV'), ('movie', 'Movie'), ('ova', 'OVA')])
    # release_date = forms.DateField(label='Дата выхода', required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    # end_date = forms.DateField(label='Дата завершения', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    # duration = forms.IntegerField(label='Длительность серии',required=False)
    # total_episodes = forms.IntegerField(label='Количество эпизодов', required=False)
    # rating = forms.DecimalField(label='Рейтинг', max_digits=3, decimal_places=1, required=False)





class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = [
            'name', 'frame_material', 'description', 'category', 'brand', 'color', 'flag',
            'size', 'price', 'is_published', 'receive_type', 'image', 'year', 'wheel_diameter',
            'tires', 'frame', 'seatpost', 'saddle', 'fork', 'takeaway', 'wheels', 'handlebar',
            'brake_system', 'shifters', 'connecting_rod_system', 'rear_derailleur', 'chain', 
            'num_gears', 'warranty_years'
        ]

        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Введите название велосипеда'
            }),
            'frame_material': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'rows': 4,
                'placeholder': 'Введите описание велосипеда'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'brand': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'color': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'flag': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'size': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'min': 0,
                'placeholder': 'Цена'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-blue-500'
            }),
            'receive_type': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full py-3 px-4 text-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'min': 1900,
                'placeholder': 'Год выпуска'
            }),
            'wheel_diameter': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'min': 0,
                'placeholder': 'Диаметр колеса'
            }),
            'tires': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Покрышки'
            }),
            'frame': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Рама'
            }),
            'seatpost': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Подседельный штырь'
            }),
            'saddle': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Седло'
            }),
            'fork': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Вилка'
            }),
            'takeaway': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Вынос'
            }),
            'wheels': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Колеса'
            }),
            'handlebar': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Руль'
            }),
            'brake_system': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Тормозная система'
            }),
            'shifters': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Манетки'
            }),
            'connecting_rod_system': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Система шатунов'
            }),
            'rear_derailleur': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Задний переключатель'
            }),
            'chain': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'placeholder': 'Цепь'
            }),
            'num_gears': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'min': 1,
                'placeholder': 'Количество передач'
            }),
            'warranty_years': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white',
                'min': 0,
                'placeholder': 'Гарантия (годы)'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['price'].initial = 100.0
        self.fields['wheel_diameter'].initial = 28.0
        self.fields['year'].initial = 2024
        self.fields['num_gears'].initial = 2
        self.fields['warranty_years'].initial = 2

        # self.fields['frame_material'].initial = FrameMaterial.objects.first()  
        # self.fields['category'].initial = Category.objects.first()
        # self.fields['brand'].initial = Brand.objects.first()  
        # self.fields['color'].initial = Color.objects.first() 
        # self.fields['flag'].initial = Flag.objects.first() 
        # self.fields['size'].initial = Size.objects.first()
        self.fields['receive_type'].initial = 'in_stock' 
        self.fields['is_published'].initial = True  