from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from cmp.models import Category, Commodity, AttributeList, Attribute, Components, Scoreset
from cmp.forms import CommodityForm
from cmp.forms import CategoryForm
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
import enum

#class CommodityFullSet(Commodity):
#    """カテゴリ毎の各商品の評価観点と特典のグラフ用データ作成クラス"""
#    def scor_calc(self, category):
#        self.commodities = category[0].commodities.all() #カテゴリのリレーション先商品を取得(related_name=commodities)
#        self.components = category[0].components.all() #カテゴリのリレーション先構成要素を取得(related_name=components)
#

POST_KIND = enum.Enum("POSR_KIND", "A B DRAW SKIP")

def category_list(request, cate):
    '''親カテゴリ一覧'''
    #return HttpResponse('カテゴリ')
    model = Article
    categories = Category.objects.all().order_by('id')
    return render_to_response('cmp_index/categories_list.html',  # 使用するテンプレート
                                {'categories': categories},       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト

def commodities_inf(request, category_id):
    '''カテゴリに属する商品一覧情報'''
    #return HttpResponse('カテゴリ')
    category = get_object_or_404(Category, link_id=category_id)  # 親カテゴリ取得
    commodities = category.commodities.all() #カテゴリのリレーション先商品を取得(related_name=commodities)
    for i in range(len(commodities)):
        #商品ごとの属性とその構成を取得し、インスタンスとして追加する
        commodities[i].components, commodities[i].attributes = commodities[i].attrscore_get()

    return render_to_response('cmp/commodity_detail_list.html',  # 使用するテンプレート
                                {'category': category, 'commodities':commodities,},       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト


class CmpPage:
    """
    商品比較用ページのクラス
    """
    def __init__(self, commodity_A, commodity_B, cmp_lists, components, cmp_lists_idx, attributelist_index):
        self.commodity_A = commodity_A
        self.commodity_B = commodity_B
        self.cmp_lists = cmp_lists
        self.components = components.attr_list[attributelist_index]
        self.cmp_lists_idx = cmp_lists_idx
        self.attributelist_index = attributelist_index
        self.A = POST_KIND.A.value
        self.B = POST_KIND.B.value
        self.DRAW = POST_KIND.DRAW.value
        self.SKIP = POST_KIND.SKIP.value



def commodity_cmp_make(request, category_id, commodity_id, cmp_cmmodity_id=None, attributelist_index=None, PAGE_ONLY=False):
    '''
    category_id : 商品カテゴリ
    commodity_id: 商品ID
    cmp_cmmodity_id : 比較商品のID
    attributelist_index : 属性リストのインデックス
    PAGE_ONLY : True 情報のみを作成する。False htmlを返す
    商品比較用のページ作成
    指定商品（A)と比較された回数が少ない商品（B)を取得し、属性ごとに出力させてく
    比較する商品が指定されている場合は、属性を切り替える
    '''

    #指定されたカテゴリを取得（商品の属するカテゴリ）
    category = get_object_or_404(Category, id=category_id)  # 親カテゴリ取得

    #対象商品が属するカテゴリの構成要素を取得
    components = get_object_or_404(Components, category=category) #対象商品を取得
    #構成要素の属性群（ManyToManyField）を、リストに落としこむ
    components.attr_list = components.attributes.all()
    #指定商品に対する比較対象商品IDリスト（比較回数が少ない順）を作成

    cmp_lists = category.cmp_lists_make(int(commodity_id))
    #比較対象は強制的に比較回数が最小のものを選択
    cmp_lists_idx = 0
    if cmp_cmmodity_id is None:
        cmp_cmmodity_id = cmp_lists[cmp_lists_idx][0]
    
    if attributelist_index is None:
        attributelist_index = 0
    attributelist_index = int(attributelist_index)
    if attributelist_index >= len(components.attr_list):
        if cmp_lists_idx < len(cmp_lists):
            attributelist_index = 0
            cmp_lists_idx = cmp_lists_idx + 1
            cmp_cmmodity_id = cmp_lists[cmp_lists_idx][0]
        else:
            return

    #対象商品と比較対象商品を取得
    commodity_A = get_object_or_404(Commodity, id=int(commodity_id)) #対象商品を取得
    try:
        commodity_B = get_object_or_404(Commodity, id=int(cmp_cmmodity_id)) #対象商品を取得
    except:
        print(int(cmp_cmmodity_id))



    cmp_page = CmpPage(commodity_A, commodity_B, cmp_lists, components, cmp_lists_idx, attributelist_index)# テンプレートに渡すデータ
    if PAGE_ONLY is True:
        return cmp_page
    else:
        return render_to_response('cmp/commodity_cmp.html',  # 使用するテンプレート
                                {   'cmp_page': cmp_page  },       # テンプレートに渡すデータ
                                context_instance=RequestContext(request))  # その他標準のコンテキスト

def commodity_cmp_post(request, commodity_A_id, commodity_B_id, attributelist_id, vote, attributelist_index):
    """
    commodity_Aとcommodity_Bをattributelist_idで
    比較した結果を格納
    """
    #import pdb; pdb.set_trace()
    commodity_A = get_object_or_404(Commodity, id=commodity_A_id) #対象商品を取得
    commodity_B = get_object_or_404(Commodity, id=commodity_B_id) #対象商品を取得
    attributelist_attr = get_object_or_404(AttributeList, id=attributelist_id) #属性を取得

    #取得した商品Aと商品B、比較属性から、商品の属性を取得
    A_attr = get_object_or_404(Attribute, obj=commodity_A, attr_name=attributelist_attr)
    B_attr = get_object_or_404(Attribute, obj=commodity_B, attr_name=attributelist_attr)
    #scoresetを取得するために、2通りの順で取得を実施
    #取得できれば、加算する
    try:
        #Aがobj1,Bがobj2のパターン
        scoreset = A_attr.obj1s_attr_for_score.get(obj2_attr=B_attr)
        obj1 = "commodity_A"
        obj2 = "commodity_B"

    except ObjectDoesNotExist:
        #Aがobj2,Bがobj1のパターン
        scoreset = A_attr.obj2s_attr_for_score.get(obj1_attr=B_attr)
        obj2 = "commodity_A"
        obj1 = "commodity_B"

    except ObjectDoesNotExist:
        return 

    if int(vote) == POST_KIND.SKIP.value:
        #skipカウンタを更新
        scoreset.skip_cnt = scoreset.skip_cnt + 1
    elif int(vote) == POST_KIND.DRAW.value:
        #甲乙つけがたいカウンタを更新
        scoreset.cannot_cnt = scoreset.cannot_cnt + 1
    elif int(vote) == POST_KIND.A.value:
        #商品Aにポイントを加算
        if obj1 == "commodity_A":
            scoreset.attr1_score = scoreset.attr1_score + 1
        elif obj2 == "commodity_A":
            scoreset.attr2_score = scoreset.attr2_score + 1
    elif int(vote) == POST_KIND.B.value:
        if obj1 == "commodity_B":
            scoreset.attr1_score = scoreset.attr1_score + 1
        elif obj2 == "commodity_B":
            scoreset.attr2_score = scoreset.attr2_score + 1
    else:
        print("invalid Vote !!!!")

    #DB更新
    scoreset.save()

    #比較用のページを作成
    attributelist_index = int(attributelist_index) + 1
    cmp_page  = commodity_cmp_make(request, commodity_A.category.id, commodity_A_id, commodity_B_id, attributelist_index, True)
    return render_to_response('cmp/commodity_cmp.html',  # 使用するテンプレート
                                {   'cmp_page': cmp_page  },       # テンプレートに渡すデータ
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
            return redirect('cmp:category_list')

    elif request.method == 'GET':
        ''' GET '''
        form = CategoryForm(instance=category)  # category インスタンスからフォームを作成

    return render_to_response('cmp/category_edit.html',
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
    paginate_by = 10  # １ページは最大10件ずつでページングする

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs['category_id'])  # 親カテゴリを読む
        commodities = category.commodities.all().order_by('id')   # カテゴリの子供の、対象を読む
        self.object_list = commodities

        context = self.get_context_data(object_list=self.object_list, category=category)    
        return self.render_to_response(context)


def commodity_edit(request, category_id, commodity_id=None):
    '''比較対象の編集:作成'''
    category = get_object_or_404(Category, pk=category_id)  # 親のカテゴリを読む
    if commodity_id:   # commodity_id が指定されている (修正時)
        commodity = get_object_or_404(Commodity, pk=commodity_id)
    else:               # commodity_id が指定されていない (追加時)
        commodity = Commodity()

    if request.method == 'POST':
        form = CommodityForm(request.POST, instance=commodity)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            commodity = form.save(commit=False)
            commodity.category = category  # この商品の、親カテゴリをセット
            commodity.save()
            #比較対象オブジェクトの生成と同時にリレーションモデルも生成
            commodity.related_models_make()
            return redirect('cmp:commodity_list', category_id=category_id)
    else:    # GET の時
        form = CommodityForm(instance=commodity)  # commodity インスタンスからフォームを作成

    return render_to_response('cmp/commodity_edit.html', #使用するテンプレート
                              {'form':form, 'category_id':category_id, 'commodity_id':commodity_id}, #テンプレートに渡すデータ
                              context_instance=RequestContext(request)) #その他標準のコンテキスト

def commodity_del(request, category_id, commodity_id):
    '''比較対象の削除'''
    commodity = get_object_or_404(Commodity, pk=commodity_id)
    commodity.delete()
    return redirect('cmp_index:commodity_list', category_id=category_id)

# Create your views here.
