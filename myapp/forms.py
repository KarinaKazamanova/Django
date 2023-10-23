from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'price',
                  'description',
                  'quantity',
                  'image']
        
class UpdateProductForm(forms.Form):
    id = forms.IntegerField(min_value=1, required=True)
    name = forms.CharField(required=False)
    price = forms.FloatField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
    quantity = forms.IntegerField(min_value=0, required=False)
    image = forms.ImageField(required=False)