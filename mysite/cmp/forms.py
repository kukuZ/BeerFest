# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cmp.models import Category, Commodity

class CommodityForm(ModelForm):
    '''比較対象のフォーム'''
    class Meta:
        model = Commodity
        fields = ('name', )

class CategoryForm(ModelForm):
    '''カテゴリのフォーム'''
    class Meta:
        model = Category
        fields = ('name',)
