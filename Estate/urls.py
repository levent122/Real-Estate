"""Estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from product.views import Index, Products, ProductDetail, AddProduct, Delete, Update, Search
from company.views import About, Contact
from user.views import Register, Login, Logout
from account.views import Profile, Settings, ChangePassword, Dashboard, AddLike, Likes, DeleteLike
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('Products/', Products, name='products'),
    path('product/<int:id>/', ProductDetail, name='product'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/<int:id>/', Profile, name='profile'),
    path('settings/', Settings, name='settings'),
    path('changePassword/', ChangePassword, name='changePassword'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('addProduct/', AddProduct, name='addProduct'),
    path('delete/<int:id>/', Delete, name='delete'),
    path('update/<int:id>/', Update, name='update'),
    path('addLike/<int:id>/', AddLike, name='addLike'),
    path('likes/', Likes, name='likes'),
    path('deleteLike/<int:id>/', DeleteLike, name='deleteLike'),
    path('search/', Search, name='search'),
    url('^', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
