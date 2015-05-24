# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cmp_index.models import Category, Commodity

class CategoryForm(ModelForm):
    '''カテゴリのフォーム'''
    class Meta:
        model = Category
        fields = ('name')

class CommodityForm(ModelForm):
    '''比較対象のフォーム'''
    class Meta:
        model = Commodity
        fields = ('name', )
