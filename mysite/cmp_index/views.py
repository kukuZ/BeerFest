from django.shortcuts import render
from django.http import HttpResponse

def category_list(request):
    '''カテゴリ一覧'''
    return HttpResponse('カテゴリ')

def category_edit(request, category_id=None):
    '''カテゴリの編集'''
    return HttpResponse('カテゴリ編集')

def category_del(request, category_id):
    '''カテゴリ削除'''
    return HttpResponse('カテゴリ削除')
# Create your views here.
