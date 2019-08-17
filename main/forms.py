# -*- coding: utf-8 -*-
from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg mt-3',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }))
    phone = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg mt-2',
        'name': 'phone',
        'placeholder': 'Ваш телефон'
    }))

    class Meta:
        model = Client
        exclude = [""]