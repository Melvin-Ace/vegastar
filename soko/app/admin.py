from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *
from .models import Cart, Product, Customer, OrderPlaced, Wishlist, Category
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.auth.models import Group

# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'firstname', 'lastname', 'email', 'mobile', 'county', 'local_town']

admin.register(Main_Category)
class Main_CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.register(Sub_Category)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products', 'quantity']

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payments']

    def customers(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def products(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def payments(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)


@admin.register(Wishlist)
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

admin.site.unregister(Group)

# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']


# class CategoryAdmin2(DraggableMPTTAdmin):
#     mptt_indent_field = "title"
#     list_display = ('tree_actions', 'indented_title',
#                     'related_products_count', 'related_products_cumulative_count')
#     list_display_links = ('indented_title',)
#
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#
#         # Add cumulative product count
#         qs = Category.objects.add_related_count(
#             qs,
#             Product,
#             'category',
#             'products_cumulative_count',
#             cumulative=True)
#
#         # Add non cumulative product count
#         qs = Category.objects.add_related_count(qs,
#                                                 Product,
#                                                 'category',
#                                                 'products_count',
#                                                 cumulative=False)
#         return qs
#
#     def related_products_count(self, instance):
#         return instance.products_count
#
#     related_products_count.short_description = 'Related products (for this specific category)'
#
#     def related_products_cumulative_count(self, instance):
#         return instance.products_cumulative_count
#
#     related_products_cumulative_count.short_description = 'Related products (in tree)'


# admin.site.register(Images)

# @admin.register(Payment)
# class PaymentModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id',
#                     'paid']
