from django.contrib import admin
from BurgerApi.models import UserProfile, Order, Ingredient, CustomerDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'ingredients', 'customer', 'price', 'orderTime')

admin.site.register(UserProfile)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ingredient)
admin.site.register(CustomerDetail)