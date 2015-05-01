from django.contrib import admin
from cmp_index.models import P_Category, Category, Commodity, Components

#admin.site.register(P_Category)
#admin.site.register(Category)
#admin.site.register(Commodity)
#admin.site.register(Components)

class P_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'p_category', 'id_ctg', 'text',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'p_category', 'id_ctg', 'text',)  # 修正リンクでクリックできる項目
admin.site.register(P_Category, P_CategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'p_category', 'num_viewer', 'num_compared', 'attribute',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'p_category', 'attribute',)  # 修正リンクでクリックできる項目
admin.site.register(Category, CategoryAdmin)

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'attribute', 'id_attr',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'category', 'attribute', 'id_attr',)  # 修正リンクでクリックできる項目
admin.site.register(Commodity, CommodityAdmin)

class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'attribute', 'id_attr',)
    list_display_links = ('id', 'attribute', 'id_attr',)
admin.site.register(Components, ComponentsAdmin)
# Register your models here.
