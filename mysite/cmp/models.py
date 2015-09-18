"""BeerFestのメイン用のモデルクラス
    比較対象用のモデル
    ランキング、ソートとか
"""
from django.db import models
from cmp_index.models import P_Category

class Category(models.Model):
    """比較対象カテゴリクラス"""
    name = models.CharField(max_length=255)
    text = models.TextField()
    link_id = models.IntegerField(default=0) #他のappとのつながりを管理するid

    # auto_now=Trueを指定すると「新規作成時」の時刻が自動的に適用される
    created_at = models.DateTimeField(('date and time created'), auto_now=True)
    # auto_now_add=Trueを指定すると保存時（毎回）の時刻が自動的に適用される
    updated_at = models.DateTimeField(('date and time updated'), auto_now_add=True)

    num_viewer = models.IntegerField(default=0)
    def get_num_commodity(self):
        """所属商品数を返す"""
        return commodity_set.all()

    def __str__(self):
        return self.name

class Commodity(models.Model):
    """比較対象オブジェクトクラス"""
    category = models.ForeignKey(Category, related_name='commodities')
    name = models.CharField(max_length=255)
    text = models.TextField()

    # 外部リンク用
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrscore_get(self):
        """Commodityが持つ属性とその属性の構成を取得し、比較結果からスコア化する"""
        components = self.category.components.all() #カテゴリのリレーション先構成要素を取得(related_name=components)
        self.components = components[0]
        self.attributes = self.attribute.all().order_by('id') #商品のリレーション先属性を取得(related_name=commodities)
        for attribute in self.attributes:
            #AttributeのScoresetを取得してスコアを算出する
            attribute.score_calc()

class AttributeList(models.Model):
    """属性一覧 全カテゴリの商品につく属性一覧 商品にはこのリストの中の属性が付く"""
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


class Attribute(models.Model):
    """属性 親となる商品に対して無数のパラメータを持てる"""
    # 商品と属性リスト内の属性からなる
    obj = models.ForeignKey(Commodity, related_name='attribute') #商品が持つ属性 Commodity.attribute.all()
    attr_name = models.ForeignKey(AttributeList, related_name='commodity') #属性が属する商品 AttributeList.commodity.all()
    name = models.CharField(max_length=255, default=(str(obj.name) + ":" + str(attr_name.name)))

    def __str__(self):
        return self.name

    def score_calc(self):
        """AttributeのScoresetを取得してスコアを算出する"""
        total_vots = 0
        score = 0

        #総比較数を算出
        scoresets1 = self.obj1s_attr_for_score.all() #商品の属性のリレーションのスコアセット取得(related_name=obj1s_attr_for_score)
        for scoreset in scoresets1:
            total_vots = total_vots + scoreset.attr1_score + scoreset.attr2_score
        scoresets2 = self.obj2s_attr_for_score.all() #商品の属性のリレーションのスコアセット取得(related_name=obj2s_attr_for_score)
        for scoreset in scoresets2:
            total_vots = total_vots + scoreset.attr1_score + scoreset.attr2_score

        #総比較数に占める対象となる組み合わせの比較数が多ければより信頼度が高いとし、その割合に応じて、組み合わせの比較で勝ち取った票をスコア化する
        for scoreset in scoresets1:
            try:
                score = score + (scoreset.attr1_score / (scoreset.attr1_score + scoreset.attr2_score)) * ((scoreset.attr1_score + scoreset.attr2_score) / total_vots)
                break
            except ZeroDivisionError:
                score = score + 0

        for scoreset in scoresets2:
            try:
                score = score + (scoreset.attr2_score / (scoreset.attr1_score + scoreset.attr2_score)) * ((scoreset.attr1_score + scoreset.attr2_score) / total_vots)
                break
            except ZeroDivisionError:
                score = score + 0

        #socreのMAX値は10とする
        score = int(score * 10)
        #self.attributesにscoreインスタンスを追加する
        self.score = score



class Components(models.Model):
    """カテゴリ別オブジェクト構成要素 CategoryとAttributeListの中間モデル"""
    category = models.ForeignKey(Category, related_name='components')
    # カテゴリ毎に存在すべき比較観点のセット
    attributes = models.ManyToManyField(AttributeList)

#    def __str__(self):
#        return (self.category.name + " Components")


class Scoreset(models.Model):
    """スコア用のセット 商品が親で、商品を親とする属性同士を比較する"""
    obj1 = models.ForeignKey(Commodity, related_name='obj1_for_score')
    obj2 = models.ForeignKey(Commodity, related_name='obj2_for_score')
    obj1_attr = models.ForeignKey(Attribute, related_name='obj1s_attr_for_score')
    obj2_attr = models.ForeignKey(Attribute, related_name='obj2s_attr_for_score')
    attr1_score = models.IntegerField(default=0)
    attr2_score = models.IntegerField(default=0)
    skip_cnt = models.IntegerField(default=0)
    cannot_cnt = models.IntegerField(default=0)
    text = models.TextField()

    # auto_now=Trueを指定すると「新規作成時」の時刻が自動的に適用される
    created_at = models.DateTimeField(('date and time created'), auto_now=True)
    # auto_now_add=Trueを指定すると保存時（毎回）の時刻が自動的に適用される
    updated_at = models.DateTimeField(('date and time updated'), auto_now_add=True)
# Create your models here.
