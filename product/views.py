from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from account.models import UserInfo
from django.contrib.auth.decorators import login_required
from .form import ProductForm
from .choices import price_choices, city_choices
from django.contrib import messages


def Index(request):

    products = Product.objects.order_by('-published_date')[:9]

    context = {
        'products':products,
        'city_choices':city_choices,
        'price_choices':price_choices
    }

    return render(request, 'product/index.html', context)



def Search(request):

    products = Product.objects.order_by('-published_date')

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)


    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        paged_products = Product.objects.filter(description__icontains= keywords)[:9]

    # City
    if 'city' in request.GET:
      city = request.GET['city']
      if city:
        paged_products = Product.objects.filter(city__iexact= city)[:9]

    # Price
    if 'price' in request.GET:
      price = request.GET['price']
      if price:
        paged_products = Product.objects.filter(price__lte= price)[:9]

    context = {
        'products':paged_products,
        'city_choices':city_choices,
        'price_choices':price_choices,
    }

    return render(request, 'product/search.html', context)



def Products(request):

    products = Product.objects.order_by('-published_date')

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
      'products': paged_products,
    }

    return render(request, 'product/products.html', context)


def ProductDetail(request, id):

    product = get_object_or_404(Product, id=id)

    context = {
        'product':product,
        'phone':UserInfo.objects.get(user_id= product.realtor.id).phone,
        'photo':UserInfo.objects.get(user_id= product.realtor.id).photo.url
    }

    return render(request, 'product/ProductDetail.html', context)



login_required(login_url= 'login')
def AddProduct(request):

    form = ProductForm(request.POST or None, request.FILES or None)

    print(request.user.id)

    if form.is_valid():

        product = form.save(commit= False)
        product.realtor_id = request.user.id
        form.save()

        return redirect('dashboard')

    context = {
        'form':form
    }

    return render(request, 'product/addProduct.html', context)



@login_required(login_url= 'login')
def Delete(request,id):

    product = get_object_or_404(Product, id= id, realtor_id= request.user.id)

    product.delete()

    messages.success(request, "Product deleted")

    return redirect('dashboard')


@login_required(login_url= 'login')
def Update(request, id):

    product = get_object_or_404(Product, id= id, realtor_id= request.user.id)

    form = ProductForm(request.POST or None, request.FILES or None, instance= product)

    if form.is_valid():

        product = form.save(commit= False)
        product.realtor_id = request.user.id
        product.save()

        return redirect('dashboard')

    context = {
        'form':form,
        'title':product.title
    }

    return render(request, 'product/update.html', context)