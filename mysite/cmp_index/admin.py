from django.contrib import admin
from cmp_index.models import P_Category

#admin.site.register(P_Category)

class P_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'category_path','last_flg', 'category_id')  # 一覧に出したい項目
    list_display_links = ('id', 'name', 'text', 'category_path','last_flg', 'category_id')  # 修正リンクでクリックできる項目
admin.site.register(P_Category, P_CategoryAdmin)


# Register your models here.
