from django.contrib import admin
from .models import Blog, Category

# Register your models here
class BlogAdmin(admin.ModelAdmin):
  exclude = ['posted']
  prepopulated_fields = { 'unique_sig': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = { 'unique_sig': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
