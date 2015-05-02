from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from cmp_index.models import Category

def category_list(request):
    '''カテゴリ一覧'''
    #return HttpResponse('カテゴリ')
    categories = Category.objects.all().order_by('id')
    return render_to_response('cmp_index/categories_list.html',  # 使用するテンプレート
                                {'categories': categories},       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト

def category_edit(request, category_id=None):
    '''カテゴリの編集'''
    return HttpResponse('カテゴリ編集')

def category_del(request, category_id):
    '''カテゴリ削除'''
    return HttpResponse('カテゴリ削除')
# Create your views here.
