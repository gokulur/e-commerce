from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login
from django.contrib import messages
from ecommerceapp.models import CustomerModal,CategoryModal,ProductModal,CartModal,OrderModal
from django.contrib.auth.decorators import login_required


#homePage
def homepage(request):
    category=CategoryModal.objects.all()
    context={'categories':category}
    return render(request,'Home.html',context)


#LOGIN-Page
def loginPage(request):
    category=CategoryModal.objects.all()
    context={'categories':category}
    return render(request,'LoginPage.html',context)

#SIGNUP-Page
def signupPage(request):
    category=CategoryModal.objects.all()
    context={'categories':category}
    return render(request,'SignUp.html',context)



#CUSTOMER-home-cart
def homeCustomerCart(request):
    category=CategoryModal.objects.all()
    productdetail=ProductModal.objects.all()
    return render(request,'customerCART.html',{'categories':category,'productdetails':productdetail})





#User/Admin-Login
def userLogin(request):
    if request.method=='POST':
        usename=request.POST['usname']
        psswrd=request.POST['password']
        user=auth.authenticate(username=usename,password=psswrd)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.info(request,'Welcome Admin')
                return redirect('adminPage')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {usename}')
                return redirect('customerPage')


#User-SignUp
def userSignUp(request):
    if request.method=='POST':
      firstName=request.POST['fname'] 
      lastName=request.POST['lname'] 
      user_email=request.POST['email']
      user_username=request.POST['uname']
      user_passwrd=request.POST['pass']
      user_cpasswrd=request.POST['cpass']
      user_address=request.POST['addre']
      user_phnnumber=request.POST['phn_num']
      user_Image=request.FILES.get('usr_img')
      if user_passwrd==user_cpasswrd:
          if User.objects.filter(username=user_username).exists():
              messages.info(request,'This Username Already Exists!!')
              return redirect('signupPage')
          elif User.objects.filter(email=user_email).exists():
              messages.info(request,'This Email Already Exists!!')
              return redirect('signupPage')
          else:
              user=User.objects.create_user(first_name=firstName,last_name=lastName,email=user_email,username=user_username,password=user_passwrd)
              user.save()
              data=User.objects.get(id=user.id)
              Customer_data=CustomerModal(Address=user_address,Customer_Image=user_Image,Phone_Number=user_phnnumber,Customer=data)
              Customer_data.save()
              messages.success(request,f'Welcome'+ data.first_name)
              return redirect('loginPage')
      else:
        messages.info(request,'Password does not match!!!')
        return redirect('signupPage')
    else:
        return redirect('signupPage')




# //////////// ADMIN ////////////

#ADMIN-Page
def adminPage(request):
    return render(request,'Admin.html')

#Admin-Add Category Page
def addCategoryPage(request):
    return render(request,'adminAddCategory.html')


#Admin-Add Category
def addCategory(request):
    if request.method=='POST':
        category_name=request.POST['categoryName']
        category=CategoryModal(Category=category_name)
        category.save()
        messages.info(request,'New Category Added')
        return redirect('adminPage')
    

#Admin-Add Page
def addProductPage(request):
    category=CategoryModal.objects.all()
    context={'categories':category}
    return render(request,'adminAddProduct.html',context)


#Admin-Add Product
def addProduct(request):
    if request.method=='POST':
        productName=request.POST['p_name']
        productDescription=request.POST['p_description']
        productQuantity=request.POST['p_quantity']
        productPrice=request.POST['p_price']
        productImage=request.FILES.get('p_img')
        productCategory=request.POST['select']
        category=CategoryModal.objects.get(id=productCategory)
        Product=ProductModal(Product_Name=productName,Product_Description=productDescription,Product_Quantity=productQuantity,Product_Price=productPrice,Product_Image=productImage,Category=category)
        Product.save()
        messages.info(request,'New Product Added')
        return redirect('adminPage')
    

#Admin-ProductDetails Page
def productDetailsPage(request):
    productdetail=ProductModal.objects.all()
    return render(request,'adminProductDetails.html',{'productdetails':productdetail})


#Admin-CustomerDetails Page
def customerDetailsPage(request):
    customer=CustomerModal.objects.all()
    return render(request,'adminCustomerDetails.html',{'customers':customer})

#Admin-EditProductsPage
def editProductPage(request,edpid):
    product=ProductModal.objects.get(id=edpid)
    category=CategoryModal.objects.all()
    return render(request,'adminProductEdit.html',{'products':product,'categories':category})

#Admin-EditProducts
def editProduct(request,pid):
    if request.method=='POST':
        product=ProductModal.objects.get(id=pid)
        product.Product_Name=request.POST['p_name']
        product.Product_Description=request.POST['p_description']
        product.Product_Quantity=request.POST['p_quantity']
        product.Product_Price=request.POST['p_price']
        product_category=request.POST['select']
        product.Category=CategoryModal.objects.get(id=product_category)
        product_oldImage=product.Product_Image
        product_newImage=request.FILES.get('p_img')
        if product_oldImage!=None and product_newImage==None:
            product.Product_Image=product_oldImage
        else:
            product.Product_Image=product_newImage
        product.save()
        return redirect('productDetailsPage')
    return render(request,'adminProductEdit.html')

#Admin-DeleteProducts
def deleteProduct(request,did):
    product=ProductModal.objects.get(id=did)
    product.delete()
    messages.info(request,'1 Product has been deleted Successfully')
    return redirect('productDetailsPage')



#Admin-DeleteCustomer
def deleteCustomer(request,cid):
    customer=CustomerModal.objects.filter(id=cid)
    customer.delete()
    messages.info(request,'1 Customer details has been deleted Successfully')
    return redirect('customerDetailsPage')


#Admin-OrderDetails
def adminOrderDetails(request):
    order=OrderModal.objects.all()
    return render( request,'AdminOrderDetails.html',{'orders':order})
    


#Customer-Product-Page
def customerproductPage(request,custid):
    category=CategoryModal.objects.all()
    categoryid=CategoryModal.objects.filter(id=custid)
    productdetail=ProductModal.objects.filter(Category=custid)
    cuser=request.user.id
    customer=CustomerModal.objects.get(Customer_id=cuser)
    return render(request,'CustomerProducts.html',{'productdetails':productdetail,'categories':category,'categoriesid':categoryid,'customers':customer})



#product-Page
def frproductPage(request,cid):
    category=CategoryModal.objects.all()
    categoryid=CategoryModal.objects.filter(id=cid)
    productdetail=ProductModal.objects.filter(Category=cid)
    return render(request,'Products.html',{'productdetails':productdetail,'categories':category,'categoriesid':categoryid})


#customer-cart
def customerCart(request):
    category=CategoryModal.objects.all()
    messages.info(request,'Your Cart is currently empty!!!')
    return render(request,'CART.html',{'categories':category})




#logout
@login_required(login_url='userLogin')
def logout(request):
    auth.logout(request)
    return redirect('loginPage')



#cart-homepage-login-required
def loginreq(request):
    if 'uid' in request.session:
        return render(request,'customerCART.html')
    return redirect('loginPage')




#Add-Cart
def addtocart(request,cartid):
    product=ProductModal.objects.get(id=cartid)
    cuser=request.user.id
    customer=CustomerModal.objects.get(Customer_id=cuser)
    cart=CartModal(Cart_Customer=customer,Cart_Product=product)
    cart.save()
    return redirect('customerPage')


#CUSTOMER-Page
def customerPage(request):
    category=CategoryModal.objects.all()
    cuser=request.user.id
    customer=CustomerModal.objects.get(Customer_id=cuser)
    return render(request,'CustomerHomePage.html',{'categories':category,'customers':customer})


#show-cart
def cartPage(request,ctid):
    category=CategoryModal.objects.all()
    pro=ProductModal.objects.get(id=ctid)
    data=CartModal.objects.filter(Cart_Customer=ctid)
    print(data)
    cuser=request.user.id
    user=CustomerModal.objects.get(Customer_id=cuser)
    print(user)
    return render(request,'customerCART.html',{'datas':data,'users':user,'categories':category,'prod':pro})


#remove-cart
def removeCart(request,remid):
    pro = CartModal.objects.get(id=remid)
    pro.delete()
    return redirect('customerPage')


#place-Order
def placeorder(request,plid):
    data =ProductModal.objects.get(id=plid)
    cuser=request.user.id
    user=CustomerModal.objects.get(Customer=cuser)
    product=OrderModal(Cart_Customer=user,Cart_Product=data)
    product.save()
    messages.info(request,'Your order has been placed!!!')
    return redirect('orderplaced')


def orderplaced(request):
    category=CategoryModal.objects.all()
    return render(request,'orderplaced.html',{'categories':category}) 
    





# ---------------------HOME-------------------
#1Image-(MEN)
def img1(request):
    obj=CategoryModal.objects.get(id=3)
    pro=ProductModal.objects.filter(Category_id=obj)
    return render(request,'Products.html',{'pros':pro})


#2Image-(WOMEN)
def img2(request):
    obj=CategoryModal.objects.get(id=5)
    pro=ProductModal.objects.filter(Category_id=obj)
    return render(request,'Products.html',{'pros':pro})


#3Image-(DEAL OF THE DAY)
def img3(request):
    obj=CategoryModal.objects.get(id=4)
    pro=ProductModal.objects.filter(Category_id=obj)
    return render(request,'Products.html',{'pros':pro})


# ---------------------CUSTOMER-------------------
#1Image-(MEN)
def cimg1(request):
    obj=CategoryModal.objects.get(id=3)
    pro=ProductModal.objects.filter(Category_id=obj)
    return render(request,'CustomerProducts.html',{'pros':pro})


#2Image-(WOMEN)
def cimg2(request):
    obj=CategoryModal.objects.get(id=5)
    pro=ProductModal.objects.filter(Category_id=obj)
    return render(request,'CustomerProducts.html',{'pros':pro})


#3Image-(DEAL OF THE DAY)
def cimg3(request):
    obj=CategoryModal.objects.get(id=4)
    pro=ProductModal.objects.filter(Category_id=obj)
    return render(request,'CustomerProducts.html',{'pros':pro})


