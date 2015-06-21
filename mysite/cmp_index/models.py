"""BeerFestの目次ページ用のモデルクラス
    サイトマップ用のモデル
    比較対象、観点などなど
"""

from django.db import models

class P_Category(models.Model):
    """カテゴリクラス"""
    name = models.CharField(max_length=255)
    category_path = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
