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
    last_flg = models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to='P_Category/', blank=True, null=True)  # upload_toは指定必須で、MEDIA_ROOT以下の同名ディレクトリにファイルがアップロードされる

    def __str__(self):
        return self.name


# Create your models here.
