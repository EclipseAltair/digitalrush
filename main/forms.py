# -*- coding: utf-8 -*-
from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={
        'id': 'name',
        'class': 'form-control form-control-lg',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }))
    phone = forms.CharField(max_length=16, required=True, widget=forms.TextInput(attrs={
        'id': 'phone',
        'class': 'form-control form-control-lg',
        'name': 'phone',
        'placeholder': '+7(___)___-__-__'
    }))
    comment = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
        'id': 'comment',
        'class': 'form-control form-control-lg',
        'name': 'comment',
        'placeholder': 'Опишите Ваши пожелания'
    }))

    class Meta:
        model = Client
        exclude = [""]
