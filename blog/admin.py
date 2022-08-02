from django.contrib import admin
from .models import Article,Category,Tag
# Register your models here.

admin.site.register(Article)
admin.site.register(Tag)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}