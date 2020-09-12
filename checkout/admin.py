from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):

    """
    Display order information in the admin panel.
    """

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 
                        'delivery_cost', 'order_total', 
                        'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name', 
                'email', 'phone_number', 
                'postcode', 'town_or_city', 'county', 'street_address1', 
                'street_address2', 'country', 'delivery_cost', 
                'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    admin_display = ('order_number', 'date', 'full_name',
                        'delivery_cost', 
                        'order_total', 'grand_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)