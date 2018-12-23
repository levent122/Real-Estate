from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'realtor', 'price', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'realtor', 'price', 'published_date', 'address', 'city', 'district', 'status', 'description']
    list_per_page = 25
    class Meta:
        model = Product