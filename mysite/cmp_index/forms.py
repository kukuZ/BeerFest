# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cmp_index.models import Category

class CategoryForm(ModelForm):
    '''書籍のフォーム'''
    class Meta:
        model = Category
        fields = ('name')
