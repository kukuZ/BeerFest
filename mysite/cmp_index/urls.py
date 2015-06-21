# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cmp_index import views

urlpatterns = [
    # カテゴリ
    url(r'^categories/$', views.p_category_list, name='p_category_list'),   # 一覧
    url(r'^categories_aa/$', views.p_category_active_list, name='p_category_active_list'),   # 一覧
]
