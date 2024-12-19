from django.shortcuts import render,get_object_or_404,redirect
from .models import *

from django.core.paginator import Paginator

from django.db.models import Q
from django.core.paginator import Paginator

from django.core.paginator import Paginator
from django.db.models import Q





def main(request,id=1):

    cat1 = get_object_or_404(Category, id=1)
    bike = Bike.objects.filter(category=cat1)
    cat2 = get_object_or_404(Category, id=3)
    hat=Bike.objects.filter(category=cat2)

    products = Bike.objects.filter(category=1)
    # bike = get_object_or_404(Bike, id=id)
    category = get_object_or_404(Category, id=id)
    # productss = Bike.objects.filter(category=category)
    product = CategoryBike.objects.filter(product=category)

    

    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
        return redirect(f'/1/?search={search}')


    sort_option = request.GET.get('sort', 'latest')
    if sort_option == 'price':
        products = products.order_by('price')  # по возрастанию цены
    elif sort_option == '-price':
        products = products.order_by('-price')  # по убыванию цены
    else:
        products = products.order_by('-created_at')  # по умолчанию, сортировка от последнего

    category_ids = request.GET.getlist('category')
    if category_ids:
        products = products.filter(Q(category__id__in=category_ids))

    brand_ids = request.GET.getlist('brand')
    if brand_ids:
        products = products.filter(Q(brand__id__in=brand_ids))

    color = request.GET.get('color')
    if color:
        products = products.filter(color__id=int(color))

    size = request.GET.get('size')
    if size:
        products = products.filter(size__id=int(size))

    material = request.GET.get('material')
    if material:
        products = products.filter(frame_material__id=int(material))

    max_price = request.GET.get('price')
    if max_price:
        products = products.filter(price__lte=int(max_price))

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'is_user_authorization': request.user.is_authenticated,
        'is_sticky': True,
        'category': Category.objects.all(),
        'brand': Brand.objects.all(),
        'material': FrameMaterial.objects.all(),
        'color': Color.objects.all(),
        'product':product,
        'cat':Category.objects.all(),
        'bike':bike,
        'hat':hat
    }

    return render(request, 'main.html', context)


# def home(request):
#     products = Bike.objects.all()
#     product=CategoryBike.objects.all()
#     search = request.GET.get('search')
#     if search:
#         products = products.filter(name__icontains=search)
    

#     sort_option = request.GET.get('sort', 'latest')
#     if sort_option == 'price':
#         products = products.order_by('price')  
#     elif sort_option == '-price':
#         products = products.order_by('-price')  
#     else:
#         products = products.order_by('-created_at')  

#     category_ids = request.GET.getlist('category')
#     if category_ids:
#         products = products.filter(Q(category__id__in=category_ids))

#     brand_ids = request.GET.getlist('brand')
#     if brand_ids:
#         products = products.filter(Q(brand__id__in=brand_ids))

#     color = request.GET.get('color')
#     if color:
#         products = products.filter(color__id=int(color))

#     size = request.GET.get('size')
#     if size:
#         products = products.filter(size__id=int(size))

#     material = request.GET.get('material')
#     if material:
#         products = products.filter(frame_material__id=int(material))

#     max_price = request.GET.get('price')
#     if max_price:
#         products = products.filter(price__lte=int(max_price))

#     paginator = Paginator(products, 6)
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)



#     if request.method == "GET":
#         is_available = request.GET.get("available")
#     if is_available == "В наличии":
#             products=products.receive_type = "В наличии"  
#     elif is_available == "Распродано":
#             products=products.receive_type = "Распродано"  

    

#     context = {
#         'products': page_obj,
#         'is_user_authorization': request.user.is_authenticated,
#         'is_sticky': True,
#         'cat': Category.objects.all(),
#         'brand': Brand.objects.all(),
#         'material': FrameMaterial.objects.all(),
#         'color': Color.objects.all(),
#         'product':product
#     }

#     return render(request, 'index.html', context)

def home(request, id=1):
    category = get_object_or_404(Category, id=id)
    products = Bike.objects.filter(category=category)

    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
    
    sort_option = request.GET.get('sort',None)
    if sort_option == 'price':
        products = products.order_by('price')
    elif sort_option == '-price':
        products = products.order_by('-price')

    category_ids = request.GET.getlist('category')
    if category_ids:
        products = products.filter(Q(category__id__in=category_ids))
    brand_ids = request.GET.getlist('brand')
    if brand_ids:
        products = products.filter(Q(brand__id__in=brand_ids))

    color = request.GET.get('color')
    if color:
        products = products.filter(color__id=int(color))

    size = request.GET.get('size')
    if size:
        products = products.filter(size__id=int(size))

    material = request.GET.get('material')
    if material:
        products = products.filter(frame_material__id=int(material))

    max_price = request.GET.get('price')
    if max_price:
        products = products.filter(price__lte=int(max_price))

    is_available = request.GET.get("available")
    if is_available == "В наличии":
        products = products.filter(availability="В наличии")
    elif is_available == "Распродано":
        products = products.filter(availability="Распродано")

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    product = CategoryBike.objects.filter(product=category)

    context = {
        'products': page_obj,
        'category': category,
        'cat': Category.objects.all(),
        'brand': Brand.objects.all(),
        'material': FrameMaterial.objects.all(),
        'color': Color.objects.all(),
        'product': product,
        'is_user_authorization': request.user.is_authenticated,
        'is_sticky': True,
    }
    return render(request, 'index.html', context)

def detail(request,id):
    product=Bike.objects.get(id=id)
    a=product.category.id
    category = get_object_or_404(Category, id=a)
    products = Bike.objects.filter(category=category)

    cat=Category.objects.all()
    size=Size.objects.all()
    color=Color.objects.all()
    images = Product_Image.objects.filter(product=product)
    context={
        'product':product,
        'image':images,
        'products':products,
        'size':size,
        'color':color,
        'cat':cat
    }
    return render(request,'detail.html',context)

def categor_elements(req, id):
    bike = Bike.objects.get(id=id)

    bikes = Bike.objects.all()

    size_list = Category.objects.all()
    material_list = FrameMaterial.objects.all()
    category_list = Category.objects.all()
    color_list = Color.objects.all()
    brand_list = Brand.objects.all()
    flag_list = Flag.objects.all()

    color = req.GET.get('color')
    if color:
        bikes = bikes.filter(color__id=int(color))

    size = req.GET.get('size')
    if size:
        bikes = bikes.filter(size__id=int(size))

    material = req.GET.get('material')
    if material:
        bikes = bikes.filter(frame_material__id=int(material))

    brand = req.GET.get('brand')
    if brand:
        bikes = bikes.filter(brand__id=int(brand))

    max_price = req.GET.get('price')
    if max_price:
        bikes = bikes.filter(price__lte=int(max_price))

    context = {
        'bike': bike,
        'products': bikes,
        'size_list': size_list,
        'material_list': material_list,
        'category_list': category_list,
        'color_list': color_list,
        'brand_list': brand_list,
        'flag_list': flag_list,
    }

    return render(req, 'index.html', context)


