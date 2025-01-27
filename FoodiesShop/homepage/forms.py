from .models import FoodImages
from django import forms

class UploadForms(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),required=True)
    category = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows':4}),required=True)
    
    cost = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}),required=True)
    
    images = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control'}),required=True)

    class Meta:
        model= FoodImages
        fields=['name','category', 'cost', 'images']


    