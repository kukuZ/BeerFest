from django.contrib import admin
from cmp.models import Commodity, Components, Category

#admin.site.register(Commodity)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'p_category', 'text',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'p_category', 'text',)  # 修正リンクでクリックできる項目
admin.site.register(Category, CategoryAdmin)

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'text',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'category', 'text',)  # 修正リンクでクリックできる項目
admin.site.register(Commodity, CommodityAdmin)

class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'attributes', 'id_attr',)
    list_display_links = ('id', 'category', 'attributes', 'id_attr',)
admin.site.register(Components, ComponentsAdmin)
# Register your models here.
