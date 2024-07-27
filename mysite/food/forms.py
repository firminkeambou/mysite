from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','item_price' ,'item_image']  # fields that should be present in the form, we don't need to have all fields
