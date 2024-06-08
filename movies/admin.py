from django.contrib import admin
from .models import Category, Movies

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['id', 'name']
    
    
@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year', 'number_in_stock', 'daily_rate' ,'category']
    exclude = ['date_created']

# Register your models here.
