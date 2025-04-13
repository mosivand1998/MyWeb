from django.contrib import admin

from .models import Category, Product , File

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enable','created_time']
    list_filter = ['is_enable','parent']
    search_files =['title']

class FileInlineAdmin(admin.StackedInline):
    model = File
    files = ['title','file_type','file','is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    search_files = ['title']
    filter_horizontal =['categories']
    inlines = [FileInlineAdmin]


