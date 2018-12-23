from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'address',
            'city',
            'district',
            'description',
            'status',
            'price',
            'bedroom',
            'bathroom',
            'garage',
            'sqft',
            'product_age',
            'air_conditioning',
            'central_heating',
            'city_views',
            'telephone',
            'internet',
            'laundry_room',
            'metro_central',
            'electric_range',
            'video',
            'photo_main',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'photo_6',
            'photo_7',
            'photo_8',
            'photo_9',
            'photo_10'
        ]
