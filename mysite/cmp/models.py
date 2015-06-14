"""BeerFestのメイン用のモデルクラス
    比較対象用のモデル
    ランキング、ソートとか
"""
from django.db import models
from cmp_index.models import Commodity

class Attribute(models.Model):
"""属性"""
    name = models.CharField(max_length=255)
    obj = models.ForeignKey(Commodity)
# Create your models here.
