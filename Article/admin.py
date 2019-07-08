from django.contrib import admin
from . models import Article, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','tags','preview_image','popular')
    list_editable = ('preview_image','popular')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article,ArticleAdmin)



