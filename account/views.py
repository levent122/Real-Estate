from django.shortcuts import render, get_object_or_404, redirect
from .models import UserInfo, Like
from product.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from .form import SettingsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



def Profile(request, id):

    user = User.objects.get(id=  id)
    user_info = UserInfo.objects.get(user_id= id)
    products = Product.objects.filter(realtor_id= id).order_by('-published_date')

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'user':user,
        'user_info':user_info,
        'products':paged_products,
        'len':len(products)
    }

    return render(request, 'account/profile.html', context)


@login_required(login_url= 'login')
def Settings(request):

    info = UserInfo.objects.get(user_id= request.user.id)

    info2 = User.objects.get(id= request.user.id)

    data ={
        'photo':info.photo,
        'birthday':info.birthday,
        'web': info.web,
        'description':info.description,
        'instagram':info.instagram,
        'twitter':info.twitter,
        'facebook':info.facebook,
        'phone':info.phone
    }

    form = SettingsForm(request.POST or None, request.FILES or None, initial= data)

    if form.is_valid():

        info.photo = form.cleaned_data.get("photo")
        info.birthday = form.cleaned_data.get("birthday")
        info.web = form.cleaned_data.get("web")
        info.description = form.cleaned_data.get("description")
        info.instagram = form.cleaned_data.get("instagram")
        info.twitter = form.cleaned_data.get("twitter")
        info.facebook = form.cleaned_data.get("facebook")
        info.phone = form.cleaned_data.get("phone")

        info.save()
        return redirect("index")

    context = {
        'form':form,
        'photo':info.photo
    }

    return render(request, 'account/settings.html', context)


@login_required(login_url= "login")
def ChangePassword(request):

    form = PasswordChangeForm(request.user, request.POST or None)

    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('index')

    context = {
        'form':form
    }

    return render(request,"account/cahngePassword.html", context)



@login_required(login_url= "login")
def Dashboard(request):

    products = Product.objects.filter(realtor_id= request.user.id).order_by('-published_date')

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products':paged_products
    }

    return render(request, 'account/dashboard.html', context)



@login_required(login_url= "login")
def AddLike(request, id):

    is_there = Like.objects.filter(user= request.user, product_id= id)

    if is_there:

        messages.warning(request, "this  is there")

    else:

        product = Like(user= request.user, product_id = id)
        product.save()
        
        messages.success(request, "Product was liked")

    return redirect('index')



@login_required(login_url= "login")
def DeleteLike(request, id):
    
    product = Like.objects.filter(user= request.user, product_id= id).delete()

    messages.success(request, "Product was deleted")

    return redirect('likes')
    

@login_required(login_url= "login")
def Likes(request):

    products = Like.objects.filter(user= request.user).order_by('-date')

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
      'products': paged_products
    }

    return render(request, 'account/likes.html', context)


