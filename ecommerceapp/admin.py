from django.contrib import admin
from ecommerceapp.models import CategoryModal, ProductModal, CustomerModal,CartModal
# Register your models here.

@admin.register(CategoryModal)
class CategoryModalDetailAdmin(admin.ModelAdmin):
    list_display=('id','Category')

@admin.register(ProductModal)
class ProductModalDetailAdmin(admin.ModelAdmin):
    list_display=('id','Category','Product_Name','Product_Description','Product_Quantity','Product_Price','Product_Image')

@admin.register(CustomerModal)
class CustomerModalDetailAdmin(admin.ModelAdmin):
    list_display=('id','Customer','Category','Product','Address','Phone_Number','Customer_Image')

@admin.register(CartModal)
class CartModalDetailAdmin(admin.ModelAdmin):
    list_display=('id','Cart_Product','Cart_Customer')