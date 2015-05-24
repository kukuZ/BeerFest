"""BeerFestの目次ページ用のモデルクラス
    サイトマップ用のモデル
    比較対象、観点などなど
"""

from django.db import models

class P_Category(models.Model):
    """カテゴリクラス"""
    p_category = models.IntegerField()
    name = models.CharField(max_length=255)
    id_ctg = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    """比較対象カテゴリクラス"""
    p_category = models.ForeignKey(P_Category)
    name = models.CharField(max_length=255)
    text = models.TextField()
    num_viewer = models.IntegerField(default=0)
    num_compared = models.IntegerField(default=0)
    attribute = models.CharField(max_length=255)
    def get_num_commodity(self):
        """所属商品数を返す"""
        return commodity_set.all()

    def __str__(self):
        return self.name
    
class Commodity(models.Model):
    """比較対象オブジェクトクラス"""
    category = models.ForeignKey(Category, related_name='commodities')
    name = models.CharField(max_length=255)
    attribute = models.CharField(max_length=255)
    id_attr = models.IntegerField()
    """T.B.D 比較観点をどうするかを考える必要あり"""

    def __str__(self):
        return self.name

class Components(models.Model):
    """オブジェクト構成要素"""
    attribute = models.CharField(max_length=255)
    id_attr = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
