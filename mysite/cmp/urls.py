# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cmp import views

urlpatterns = [
    # カテゴリ
    url(r'^commodities/(?P<category_id>\d+)/$', views.commodities_inf, name='commodities_inf'),   # カテゴリ情報
    url(r'^commodity/add/(?P<category_id>\d+)/$', views.commodity_edit, name='commodity_add'),        # 登録
    url(r'^cmpare/(?P<category_id>\d+)/(?P<commodity_id>\d+)/$', views.commodity_cmp_make, name='commodity_cmp_make'),        # 商品比較
    url(r'^cmpare_post/(?P<commodity_A_id>\d+)/(?P<commodity_B_id>\d+)/(?P<attributelist_id>\d+)/(?P<vote>\d+)/(?P<attributelist_index>\d+)/$', views.commodity_cmp_post, name='commodity_cmp_post'),        # 登録
    #url(r'^cmpare_post/(?P<cmp_page>\d+)/$', views.commodity_cmp_post, name='commodity_cmp_post'),        # 登録
    #url(r'^category/add/$', views.category_edit, name='category_add'),  # 登録
    #url(r'^category/mod/(?P<category_id>\d+)/$', views.category_edit, name='category_mod'),  # 修正
    #url(r'^category/del/(?P<category_id>\d+)/$', views.category_del, name='category_del'),   # 削除
    url(r'^commodity/(?P<category_id>\d+)/$', views.CommodityList.as_view(), name='commodity_list'),  # 一覧
    url(r'^commodity/mod/(?P<category_id>\d+)/(?P<commodity_id>\d+)/$', views.commodity_edit, name='commodity_add'),  # 修正
    url(r'^commodity/del/(?P<category_id>\d+)/(?P<commodity_id>\d+)/$', views.commodity_del, name='commodity_del'),   # 削除
]
