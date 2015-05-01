# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cmp_index import views

urlpatterns = [
    # カテゴリ
    url(r'^category/$', views.category_list, name='category_list'),   # 一覧
    url(r'^category/add/$', views.category_edit, name='category_add'),  # 登録
    url(r'^category/mod/(?P<category_id>\d+)/$', views.category_edit, name='category_mod'),  # 修正
    url(r'^category/del/(?P<category_id>\d+)/$', views.category_del, name='category_del'),   # 削除
]
