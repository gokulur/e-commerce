from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginPage',views.loginPage,name='loginPage'),
    path('adminPage',views.adminPage,name='adminPage'),
    path('customerPage',views.customerPage,name='customerPage'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('signupPage',views.signupPage,name='signupPage'),
    path('userSignUp',views.userSignUp,name='userSignUp'),
    path('addCategoryPage',views.addCategoryPage,name='addCategoryPage'),
    path('addCategory',views.addCategory,name='addCategory'),
    path('addProductPage',views.addProductPage,name='addProductPage'),
    path('addProduct',views.addProduct,name='addProduct'),
    path('productDetailsPage',views.productDetailsPage,name='productDetailsPage'),
    path('customerDetailsPage',views.customerDetailsPage,name='customerDetailsPage'),
    path('frproductPage/<int:cid>',views.frproductPage,name='frproductPage'),
    path('editProductPage/<int:edpid>',views.editProductPage,name='editProductPage'),
    path('editProduct/<int:pid>',views.editProduct,name='editProduct'),
    path('deleteProduct/<int:did>',views.deleteProduct,name='deleteProduct'),
    path('deleteCustomer/<int:cid>',views.deleteCustomer,name='deleteCustomer'),
    path('addtocart/<int:cartid>',views.addtocart,name='addtocart'),
    path('logout',views.logout,name='logout'),

    path('customerCart',views.customerCart,name='customerCart'),
    path('homeCustomerCart',views.homeCustomerCart,name='homeCustomerCart'),
    path('customerproductPage/<int:custid>',views.customerproductPage,name='customerproductPage'),
    path('cartPage/<int:ctid>',views.cartPage,name='cartPage'),

    #Home-IMAGES
    path('img1',views.img1,name='img1'),
    path('img2',views.img2,name='img2'),
    path('img3',views.img3,name='img3'),

     #Customer-IMAGES
    path('cimg1',views.cimg1,name='cimg1'),
    path('cimg2',views.cimg2,name='cimg2'),
    path('cimg3',views.cimg3,name='cimg3'),

    path('loginreq',views.loginreq,name='loginreq'),

    path('removeCart/<int:remid>',views.removeCart,name='removeCart'),
    path('placeorder/<int:plid>',views.placeorder,name='placeorder'),
    path('orderplaced',views.orderplaced,name='orderplaced'),


    path('adminOrderDetails',views.adminOrderDetails,name='adminOrderDetails')

    
    ]