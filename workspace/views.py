from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404 

# from slugify import slugify
from django.contrib import messages
import logging

from bike.models import Bike , Product_Image,Category

from django.urls import reverse

from django.utils.text import slugify
from .forms import BikeForm

logger = logging.getLogger(__name__)


def main(request):
    news = Bike.objects.all()
    cat=Category.objects.all()
    page = request.GET.get('page', 1) or 1
    pagin = Paginator(news, 10)
    news = pagin.get_page(page)
    return render(request, 'workspace/index.html', {'news': news,"cat":cat})


def create_bike(request):
    form = BikeForm()
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save()
            messages.success(request, 'Карточка успешно создана!')
            return redirect('/1')
        print(form)
    else:
        form = BikeForm()
    return render(request, 'workspace/create.html', {'form': form})

def update_bike(request,id):
    bike = get_object_or_404(Bike, id=id)
    category=bike.category

    form = BikeForm()
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES, instance=bike)
        if form.is_valid():
            bike=form.save()
            messages.success(request, f'Продукт "{bike.name}" обновлен!')
            return redirect(f'/{category.id}') 
    else:
        form = BikeForm(instance=bike)
    return render(request, 'workspace/update.html', {'form': form, 'bike': bike})


def delete(request, id):
    product = get_object_or_404(Bike, id=id)
    category=product.category

    product.delete()
    messages.success(request, 'Продукт успешно удалён!')
    return redirect(f'/{category.id}') 

# def create_bike(request):
#     form=BikeForm()
#     if request.method == 'POST':
#         form = BikeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')  # Перенаправление на страницу с велосипедом
#     else:
#         form = BikeForm()
#     return render(request, 'workspace/create.html', {'form': form})


# def main(request):
#     product=Product.objects.all()
#     genres = Genre.objects.all()
#     context = {
#         'genres': genres,
#         'product': product,
#     }
#     return render(request,'workspace/index.html',context)








# def create_anime(request):
#     form = NewsForm()

#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)  # Обратите внимание на request.FILES для обработки изображений
#         if form.is_valid():
#             # Создание объекта новостей
#             news = Product(
#                 title=form.cleaned_data['title'],
#                 original_title=form.cleaned_data['original_title'],
#                 poster=form.cleaned_data['poster'],
#                 description=form.cleaned_data['description'],
#                 author=form.cleaned_data['author'],
#                 category=form.cleaned_data['category'],
#                 is_published=form.cleaned_data['is_published'],
#                 status=form.cleaned_data['status'],
#                 type=form.cleaned_data['type'],
#                 release_date=form.cleaned_data['release_date'],
#                 end_date=form.cleaned_data['end_date'],
#                 duration=form.cleaned_data['duration'],
#                 total_episodes=form.cleaned_data['total_episodes'],
#                 rating=form.cleaned_data['rating']
#             )
#             news.save()

#             # Обработка тегов и жанров
#             news.tags.set(form.cleaned_data['tags'])
#             news.genres.set(form.cleaned_data['genres'])

#             messages.success(request, 'Новость успешно создана!')
#             return redirect('/')  # Перенаправление на страницу со списком новостей или другую

#     else:
#         form = NewsForm()

#     return render(request, 'workspace/create.html', {'form': form})




# def delete_news(request, id):
#     product = get_object_or_404(Product, id=id)

#     product.delete()
#     messages.success(request, 'Продукт успешно удалён!')
#     return redirect('/')  




# def update_anime(request, id):

#     news = get_object_or_404(Product, id=id)
#     form = NewsForm(instance=news)

#     if request.method == 'POST':
#         form = NewsForm(data=request.POST, files=request.FILES, instance=news)
#         if form.is_valid():
#             news = form.save()

#             messages.success(request, f'The news "{news.title}" was updated successfully!')
#             return redirect('/')

#         messages.error(request, 'Please correct some errors!')

#     return render(request, 'workspace/update.html', {
#         'form': form,
#         'news': news,
#     })
