from django.apps import AppConfig


class MainCategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_category'
    verbose_name = 'Main Categories'
    order = 1


class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'
    verbose_name = 'Categories'
    order = 2


class SubCategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sub_category'
    verbose_name = 'Sub Categories'
    order = 3


class ProductModelAdmin(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'title'
    verbose_name = 'Product'
    order = 4


class CustomerModelAdmin(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'id'
    verbose_name = 'Customer'
    order = 5


class OrderPlacedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_placed'
    verbose_name = 'Orders'
    order = 6


# main_category/__init__.py
default_app_config = 'main_category.apps.MainCategoryConfig'

# category/__init__.py
default_app_config = 'category.apps.CategoryConfig'

# sub_category/__init__.py
default_app_config = 'sub_category.apps.SubCategoryConfig'

# product/__init__.py
default_app_config = 'product.apps.ProductConfig'

# customer/__init__.py
default_app_config = 'customer.apps.CustomerConfig'

# order_placed/__init__.py
default_app_config = 'order_placed.apps.OrderPlacedConfig'
