"""BeerFestのメイン用のモデルクラス
    比較対象用のモデル
    ランキング、ソートとか
"""
from django.db import models
from cmp_index.models import P_Category

class Category(models.Model):
    """比較対象カテゴリクラス"""
    p_category = models.ForeignKey(P_Category)
    name = models.CharField(max_length=255)
    text = models.TextField()

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
    """T.B.D 比較観点をどうするかを考える必要あり"""

    # 外部リンク用
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Components(models.Model):
    """カテゴリ別オブジェクト構成要素"""
    category = models.ForeignKey(Category, related_name='components')
    # カテゴリ毎に存在すべき比較観点のセット
    attributes = models.CommaSeparatedIntegerField(max_length=255)
    id_attr = models.IntegerField()

    def __str__(self):
        return self.name

class Attribute(models.Model):
    """属性 親となる商品に対して無数のパラメータを持てる"""
    obj = models.ForeignKey(Commodity)
    # 同一の観点を表すname,ID
    name = models.CharField(max_length=255)
    attr_id = models.IntegerField(default=0)
    text = models.TextField()


class Scoreset(models.Model):
    """スコア用のセット"""
    obj = models.ForeignKey(Commodity)
    attr1_2 = models.ManyToManyField(Attribute)
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
