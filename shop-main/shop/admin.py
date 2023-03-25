from django.contrib import admin
from .models import *


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', "name", 'slug', 'photo', 'price', "specification", "warranty", "category")
#     search_fields = ("name", 'slug', 'photo', 'price', "specification", "warranty", "category")
#     list_editable = ("name", 'slug', 'photo', 'price', "specification", "warranty", "category")
#
#
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_number', 'email')
#     search_fields = ('name', 'phone_number', 'email')
#     list_filter = ('name', 'phone_number', 'email')
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('product', 'time', 'total_price', 'client')
#     search_fields = ('product', 'time', 'total_price', 'client')
#     list_filter = ('product', 'time', 'total_price', 'client')


admin.site.register(Category)# , CategoryAdmin)
admin.site.register(Product)# , ProductAdmin)
admin.site.register(Client)# , ClientAdmin)
admin.site.register(Order)# , OrderAdmin)
admin.site.register(Spec_gadget)
