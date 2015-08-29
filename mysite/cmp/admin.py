from django.contrib import admin
from cmp.models import Commodity, Components, Category, Attribute, Scoreset, AttributeList

#admin.site.register(Commodity)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'text', 'link_id',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'text', 'link_id',)  # 修正リンクでクリックできる項目
admin.site.register(Category, CategoryAdmin)

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'text',)  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'category', 'text',)  # 修正リンクでクリックできる項目
admin.site.register(Commodity, CommodityAdmin)

class ComponentsAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_display_links = ('category',)
admin.site.register(Components, ComponentsAdmin)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('obj', 'attr_name', 'name',)
    list_display_links = ('obj', 'attr_name', 'name',)
admin.site.register(Attribute, AttributeAdmin)

class ScoresetAdmin(admin.ModelAdmin):
    list_display = ('obj1', 'obj2', 'obj1_attr', 'obj2_attr', 'attr1_score', 'attr2_score', 'skip_cnt', 'cannot_cnt', 'text', 'created_at', 'updated_at',)
    list_display_links = ('obj1', 'obj2', 'obj1_attr', 'obj2_attr', 'attr1_score', 'attr2_score', 'skip_cnt', 'cannot_cnt', 'text', 'created_at', 'updated_at',)
admin.site.register(Scoreset, ScoresetAdmin)

class AttributeListAdmin(admin.ModelAdmin):
    list_display = ('name', 'text',)
    list_display_links = ('name', 'text',)
admin.site.register(AttributeList, AttributeListAdmin)
# Register your models here.
