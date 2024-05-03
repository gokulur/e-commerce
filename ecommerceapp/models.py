from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


#CategoryModal
class CategoryModal(models.Model):
    Category=models.CharField(max_length=250)


#ProductsModal
class ProductModal(models.Model):
    Category=models.ForeignKey(CategoryModal,on_delete=models.CASCADE,null=True)
    Product_Name=models.CharField(max_length=250)
    Product_Description=models.CharField(max_length=250)
    Product_Quantity=models.CharField(max_length=100)
    Product_Price=models.CharField(max_length=100)
    Product_Image=models.ImageField(upload_to="image/",null=True)


#CustomerModal
class CustomerModal(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Category=models.ForeignKey(CategoryModal,on_delete=models.CASCADE,null=True)
    Product=models.ForeignKey(ProductModal,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=250)
    Phone_Number=models.CharField(max_length=250)
    Customer_Image=models.ImageField(upload_to="image/",null=True)


#CartModal
class CartModal(models.Model):
    Cart_Product=models.ForeignKey(ProductModal,on_delete=models.CASCADE,null=True)
    Cart_Customer=models.ForeignKey(CustomerModal,on_delete=models.CASCADE,null=True)



class OrderModal(models.Model):
    Cart_Product=models.ForeignKey(ProductModal,on_delete=models.CASCADE,null=True)
    Cart_Customer=models.ForeignKey(CustomerModal,on_delete=models.CASCADE,null=True)
    Customer_name=models.CharField(max_length=250)
    Product_name=models.CharField(max_length=250)
    Quantity=models.CharField(max_length=250)
    Address=models.CharField(max_length=250)
    Phone_Number=models.CharField(max_length=250)
    Order_date=models.DateField(auto_now_add=True)
    