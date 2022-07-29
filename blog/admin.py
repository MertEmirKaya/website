from django.contrib import admin
from .models import Article,Category
# Register your models here.

admin.site.register(Article)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}