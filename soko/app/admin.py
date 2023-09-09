from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Product
from .models import Main_Category, Category, Sub_Category, Product, Customer, Cart, OrderPlaced, Wishlist
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

# Register your models here.
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'firstname', 'lastname', 'email', 'mobile', 'county', 'local_town', 'birthday', 'sex']

class Main_CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['man_name']

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['cat_name', 'main_category']
    raw_id_fields = ['main_category']
    search_fields = ['man_name']


class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    raw_id_fields = ['category']
    search_fields = ['title', 'category__name']


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'category', 'sub_category']
    search_fields = ['title', 'category__name', 'sub_category__name']
    raw_id_fields = ['category', 'sub_category']
    autocomplete_fields = ['category', 'sub_category']


class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payments']

    def customers(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.firstname)

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def payments(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)


class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

class ProductAdmin:
    pass

# admin.site.register(Product, ProductAdmin)

class Images:
    pass


admin.site.register(Customer, CustomerModelAdmin)
admin.site.register(Main_Category, Main_CategoryModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Sub_Category, SubCategoryModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.register(Cart)
admin.site.register(OrderPlaced)
admin.site.register(Wishlist)

admin.site.unregister(Group)


