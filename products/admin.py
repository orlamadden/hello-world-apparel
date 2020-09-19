from django.contrib import admin
from .models import Product, Category, Review

""" 
Customises what fields to display in
the Product admin dashboard
"""
class ProductAdmin(admin.ModelAdmin):
    # what fields to display
    list_display = (
        'name',
        'category',
        'price',
    )
    
    # orders inventory a-z by name
    ordering = ('name',)

""" 
Customises what fields to display in
the Category admin dashboard
"""
class CategoryAdmin(admin.ModelAdmin):
    # what fields to display
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    To display the below fields to the Review admin panel.
    """
    list_display = (
        'user',
        'comment',
        'product',
        'rating'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
