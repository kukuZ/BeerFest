from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from cmp.models import Category
from cmp.forms import CommodityForm
from django.views.generic.list import ListView

def category_list(ListView):
    '''親カテゴリ一覧'''
    #return HttpResponse('カテゴリ')
    model = Article
    categories = Category.objects.all().order_by('id')
    return render_to_response('cmp_index/categories_list.html',  # 使用するテンプレート
                                {'categories': categories},       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト

def category_edit(request, category_id=None):
    '''カテゴリの編集'''
#    return HttpResponse('カテゴリ編集')
    if category_id:   # category_id が指定されている (修正時)
        category = get_object_or_404(Category, pk=category_id)
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
#    return HttpResponse('カテゴリ削除')
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('cmp_index:category_list')


class CommodityList(ListView):
    '''比較対象の一覧'''
    context_object_name='commodities'
    template_name='cmp_index/commodity_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs['category_id'])  # 親カテゴリを読む
        commodities = category.commodities.all().order_by('id')   # カテゴリの子供の、対象を読む
        self.object_list = commodities

        context = self.get_context_data(object_list=self.object_list, category=category)    
        return self.render_to_response(context)


def commodity_edit(request, category_id, commodity_id=None):
    '''比較対象の編集'''
    category = get_object_or_404(Category, pk=category_id)  # 親のカテゴリを読む

    if commodity_id:   # commodity_id が指定されている (修正時)
        commodity_id = get_object_or_404(Commodity, pk=commodity_id)
    else:               # impression_id が指定されていない (追加時)
        commodity = Commodity()

    if request.method == 'POST':
        form = CommodityForm(request.POST, instance=commodity)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            commodity = form.save(commit=False)
            commodity.category = category  # この商品の、親カテゴリをセット
            commodity.save()
            return redirect('cmp_index:commodity_list', category_id=category_id)
    else:    # GET の時
        form = CommodityForm(instance=commodity)  # commodity インスタンスからフォームを作成

    return render_to_response('cmp_index/commodity_edit.html',
                              dict(form=form, category_id=category_id, commodity_id=commodity_id),
                              context_instance=RequestContext(request))

def commodity_del(request, category_id, commodity_id):
    '''比較対象の削除'''
    commodity = get_object_or_404(Commodity, pk=commodity_id)
    commodity.delete()
    return redirect('cmp_index:commodity_list', category_id=category_id)

# Create your views here.
