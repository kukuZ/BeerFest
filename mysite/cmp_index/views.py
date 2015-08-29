from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from cmp_index.models import P_Category
from django.views.generic.list import ListView

def p_category_list(request):
    '''親カテゴリ一覧'''
    #return HttpResponse('カテゴリ')
#    p_categories = P_Category.objects.all().order_by('id')
    p_categories = P_Category.objects.filter(last_flg=1).order_by('name')
    return render_to_response('cmp_index/p_categories_list.html',  # 使用するテンプレート
                                {'p_categories': p_categories},       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト

def p_category_active_list(request, index, num):
    '''任意のインデックスから任意のカテゴリ数分'''
    #return HttpResponse('カテゴリ')
    p_categories = P_Category.objects.all().order_by('id')
    p_categorise_set = p_categorise[index:(index + num)]
    return render_to_response('cmp_index/p_categories_list.html',  # 使用するテンプレート
                                {'p_categories': p_categories},       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト

# Create your views here.

