#from django import forms
from .models import Advertisement
from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput, FileInput
from django.core.exceptions import ValidationError


class AdvertisementModelForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['title']
        if data.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с "?"')
        return data

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'is_auction', 'image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control-lg'}),
            'is_auction': CheckboxInput(attrs={'class': 'form-control-lg'}),
            'image': FileInput(attrs={'class': 'form-control-lg'})
        }

# class AdvertisementForm(forms.Form):
#     title =forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
#     description =forms.CharField(widget=forms.Textarea)    # многострочное поле
#     price =forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control-lg'}))
#     is_auction =forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control-lg'}))      # необязательный параметр
#     image =forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-lg'}))

