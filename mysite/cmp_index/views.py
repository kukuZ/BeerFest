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
#    return HttpResponse('カテゴリ編集')
    if category_id:   # category_id が指定されている (修正時)
        category = get_object_or_404(category, pk=category_id)
    else:
        category = Category()

    if request.method == 'POST':
        ''' POST '''
        form = CategoryForm(request.POST, instance=category) # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            category = form.save(commit=False)
            category.save()
            return redirect('cmp_index:category_list')

    elif request.method == 'GET':
        ''' GET '''
        form = CategoryForm(instance=category)  # category インスタンスからフォームを作成

    return render_to_response('cmp_index/category_edit.html',
                              dict(form=form, category_id=category_id),
                              context_instance=RequestContext(request))


def category_del(request, category_id):
    '''カテゴリ削除'''
    return HttpResponse('カテゴリ削除')

# Create your views here.

