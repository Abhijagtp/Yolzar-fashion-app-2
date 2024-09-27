"""
URL configuration for fashion_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    
    path('contactpage/',v.contact_view,name='contactpage'),
    path('login/',v.login_view,name='login'),
    path('register/',v.register_view,name='register'),
    path('logout/',v.logout_view,name='logout'),
    path('cart/',v.cart_list,name='cart'),
    path('addtocart/<int:pid>',v.add_to_cart,name='addtocart'),
    path('wishlist/',v.wishlist_view,name='wishlist'),
    path('addtowishlist/<int:pid>',v.add_to_wishlist,name='addtowishlist'),
    path('delete_item_cart/<int:pid>',v.del_item_cart_view,name='delete_item_cart'),
    path('delete_item_wishlist/<int:pid>',v.del_item_wishlist_view,name='delete_item_wishlist'),
    path('shop/', v.filter_view, name='shop'),
    path('filter/<int:category_id>/', v.filter_view, name='filter'),
    path('search/', v.filter_view, name='search'),
    path('checkout/',v.checkout_view, name = 'checkout'),
    path('order/',v.order_view,name='order'),
    path('payment/',v.payment_view,name='payment'),
    path('paymentdone/',v.paymentdone_view,name='paymentdone'),
    path('orderconfirm/',v.orderconfirm_view,name='orderconfirm'),
    # 
    path('paypal/payment/', v.paypal_payment_view, name='paypal_payment'),
    path('paypal/execute/', v.paypal_execute_view, name='paypal_execute'),
    path('shoppage/<int:pro>',v.shoppage_view,name='shoppage'),
    path('profile/', v.profile_view, name='profile'),

    

    # forget password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name ='password_reset_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name='password_reset_complete'),

]
