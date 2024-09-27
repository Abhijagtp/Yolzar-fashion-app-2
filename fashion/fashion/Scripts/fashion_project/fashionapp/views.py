from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Product
from .models import Cart,Wishlist,Category,OrderYolzar,OrderItem
from django.core.mail import send_mail



# Create your views here.

def home(request):
    return render(request,"index.html")

# # shop view

# def shop_view(request):
   
#     products= Product.objects.all()  # sab products liya
   
  
#     context = {
#               'products': products,
              
#              }
#     return render(request, 'shop.html', context)

# filter
# filter1 ---------------------------------------------------------

# def filter_view(request,pid):
#     products = Product.objects.all()  # sab products liya
#     categorys = Category.objects.all()
#     pro = set()  
#     for i in products:
#        pro.add(i.category)
#        products = Category.objects.filter(pro=pid)

#     context = {
#               'products': products,
#               'pro':pro
#              }
    
#     return render(request, 'shop.html', context)

#filter 2-------------------------------------

# def filter_view(request, pid=None):
    
#     categories = Category.objects.all() # sab category liya

    
#     if pid and pid != "all":                                    # agar category id hai then give that products if not then show all
#         products = Product.objects.filter(category__id=pid)
#     else:
#         products = Product.objects.all()

#     context = {
#         'products': products,
#         'categories': categories,
#         'selected_category': pid
#     }
#     return render(request, 'shop.html', context)

# filter3 -----------------------------------------

# def filter_view(request, category_id=None):
#     # Get all categories
#     categories = Category.objects.all()

#     # Start with all products
#     products = Product.objects.all()

#     # Filter by category if a category_id is provided
#     if category_id and category_id != "all":
#         products = products.filter(category__id=category_id)

#     # Filter by search query if provided
#     search_query = request.GET.get('search_query')
#     if search_query:
#         products = products.filter(p_name__icontains=search_query)

#     context = {
#         'products': products,
#         'categories': categories,
#         'selected_category': category_id,
#         'search_query': search_query,
#     }
#     return render(request, 'shop.html', context)

def filter_view(request, category_id=None):
    # Get all categories
    categories = Category.objects.all()

    # Default category_id to 'all' or the first category 
    if category_id is None:
        category_id = 'all'

    # get  all products
    products = Product.objects.all()

    # Filter by category if a category_id is provided
    if category_id != "all":
        products = products.filter(category__id=category_id)

    # Filter by search query if provided
    search_query = request.GET.get('search_query')
    if search_query:
        products = products.filter(p_name__icontains=search_query)

    # Filter by price range if provided
    price_range = request.GET.get('price_range')
    if price_range:
        min_price, max_price = map(int, price_range.split('_'))
        products = products.filter(p_price__gte=min_price, p_price__lte=max_price)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_id if category_id != 'all' else  None,
        'search_query': search_query,
        'selected_price_range': price_range,  # Add this to preserve the selected price range
    }
    return render(request, 'shop.html', context)


# filter 4------------------------------------------------------------


# def filter_view(request, category_id=None):
#     categories = Category.objects.all()
    
#     # Get the selected price range from the request
#     price_range = request.GET.get('price_range')
    
#     # Get the search query
#     search_query = request.POST.get('search', '')

#     # If a category ID is provided, filter by category
#     if category_id and category_id != "all":
#         products = Product.objects.filter(category__id=category_id)
#     else:
#         products = Product.objects.all()

#     # Apply price filtering
#     if price_range:
#         if price_range == "100_500":
#             products = products.filter(p_price__gte=100, p_price__lte=500)
#         elif price_range == "500_1000":
#             products = products.filter(p_price__gte=500, p_price__lte=1000)
#         elif price_range == "1000_15000":
#             products = products.filter(p_price__gte=1000, p_price__lte=15000)

#     # Apply search filtering
#     if search_query:
#         products = products.filter(p_name__icontains=search_query)

#     context = {
#         'products': products,
#         'categories': categories,
#         'selected_category': category_id,
#         'selected_price_range': price_range,
#         'search_query': search_query,
#     }
#     return render(request, 'shop.html', context)





# search view 

# def search_view(request):
#     srch = request.POST.get('srch')
#     products= Product.objects.filter(p_name=srch)

#     context ={
#         'pro':products
#     }

#     return render(request,'shop.html',context)
def search_view(request):
    search_query = request.POST.get('search', '')

    if search_query:
        products = Product.objects.filter(p_name__icontains=search_query)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query
    }
    return render(request, 'shop.html', context)

# def search_view(request):
#     srch = request.POST.get('search')  
#     if srch:
#         products = Product.objects.filter(p_name__icontains=srch)
#     else:
#         products = Product.objects.all()

#     context = {
#         'products': products,
#         'search_query': srch 
#     }
#     return render(request, 'shop.html', context)


def contact_view(request):
    return render (request,'contact.html')

# login page
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['uid']=user.id
            login(request, user)  # This will create a session
            messages.success(request, "Login successful!")
            return redirect('/')  # Redirect to a named URL pattern (home)
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

# logout page
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect ('/')


# register page


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address")
            return render(request, 'register.html')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, 'register.html')


# Cart page 
# def add_to_cart(request,pid):
#     product_id = Product.objects.get(id=pid)
#     uid = request.session.get('uid')
#     user_id = User.objects.get(id=uid)
#     c=Cart()
#     c.Product = product_id
#     c.user = user_id
#     c.save()
#     messages.success(request,"Item added to cart")
#     return redirect('/shop')

from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Cart
from django.contrib.auth.models import User

def add_to_cart(request, pid):
    if not request.session.get('uid'):
        messages.success(request,'log in first')
        return redirect('login')  # Redirect to login if the user is not logged in
    
    product = get_object_or_404(Product, id=pid)
    uid = request.session.get('uid')
    user = get_object_or_404(User, id=uid)

    # Check if the product is already in the cart for this user
    cart_item, created = Cart.objects.get_or_create(user=user, Product=product)

    if not created:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item quantity updated in the cart.")
    else:
        # If the product is not in the cart, set the quantity to 1
        cart_item.quantity = 1
        cart_item.save()
        messages.success(request, "Item added to cart.")

    return redirect('/shop')

# def cart_list(request):
#     uid=request.session.get('uid')
#     # user_id = User.objects.get(id=uid)
#     cl=Cart.objects.filter(user=uid)
#     context = {'cl':cl}
#     return render(request,"cartlist.html",context)

def cart_list(request):
    if not request.session.get('uid'):
        messages.success(request,'Log in first')
        return redirect('login')  # Redirect to login if the user is not logged in

    uid = request.session.get('uid')
    user = get_object_or_404(User, id=uid)

    # Fetch all cart items for the user
    cart_items = Cart.objects.filter(user=user)
    
    # Calculate subtotal for each cart item
    for item in cart_items:
        item.subtotal = item.Product.p_price * item.quantity
    
    context = {'cart_items': cart_items}
    return render(request, "cartlist.html", context)

# WISHLIST
# def wishlist_view(request):
#     uid=request.session.get('uid')
#     # user_id = User.objects.get(id=uid)
#     cl=Wishlist.objects.filter(user=uid)
#     context = {'cl':cl}
#     return render(request,'wishlist.html',context)
def wishlist_view(request):
    if not request.session.get('uid'):
        messages.success(request, 'Log in first')
        return redirect('login')  # Redirect to login if the user is not logged in

    uid = request.session.get('uid')
    user = get_object_or_404(User, id=uid)

    # Fetch all wishlist items for the user
    wishlist_items = Wishlist.objects.filter(user=user)
    
    context = {'wishlist_items': wishlist_items}
    return render(request, 'wishlist.html', context)

# def add_to_wishlist(request,pid):
#     product_id = Product.objects.get(id=pid)
#     uid = request.session.get('uid')
#     user_id = User.objects.get(id=uid)
#     c=Wishlist()
#     c.Product = product_id
#     c.user = user_id
#     c.save()
#     messages.success(request,"Item added to Wishlist")

#     return redirect('/shop')
def add_to_wishlist(request, pid):
    if not request.session.get('uid'):
        messages.success(request, 'Log in first')
        return redirect('login')  # Redirect to login if the user is not logged in

    product = get_object_or_404(Product, id=pid)
    uid = request.session.get('uid')
    user = get_object_or_404(User, id=uid)

    # Check if the product is already in the wishlist for this user
    wishlist_item, created = Wishlist.objects.get_or_create(user=user, Product=product)

    if not created:
        messages.info(request, "Item is already in your wishlist.")
    else:
        messages.success(request, "Item added to wishlist.")

    return redirect('/shop')

# delete item

def del_item_cart_view(request,pid):
    delitem = Cart.objects.get(id=pid)
    delitem.delete()
    messages.warning(request,"Item removed")
    return redirect ("/cart")

def del_item_wishlist_view(request,pid):
    delitem = Wishlist.objects.get(id=pid)
    delitem.delete()
    messages.warning(request,"Item removed")
    return redirect ("/wishlist")

def shoppage_view(request,pro):
    # pid = Product.objects.get(id=pro)
    pl = Product.objects.filter(id=pro)
    context  = {
        'pl':pl
    }
    return render(request,"shopage.html",context)
# filter

   
    # price_range = request.GET.get('price_range')
    
    # Start with all products
    # products = Product.objects.all()
    
    # Filter by category if selected
    # if category:
    #     products = Product.objects.filter(category=category)
    
    # # Filter by price range if selected
    # # if price_range:
    # #     if price_range == "100_500":
    # #         products = products.filter(p_price__gte=100, p_price__lte=500)
    # #     elif price_range == "500_1000":
    # #         products = products.filter(p_price__gte=500, p_price__lte=1000)
    # #     elif price_range == "1000_15000":
    # #         products = products.filter(p_price__gte=1000, p_price__lte=15000)
    
    # context = {'products': products}
    # return render(request, 'shop.html', context)    


# def checkout_view(request):
#     uid=request.session.get('uid')
#     # user_id = User.objects.get(id=uid)
#     cl=Cart.objects.filter(user=uid)
#     context = {'cl':cl}
#     return render(request,"checkout.html",context)

def checkout_view(request):
    uid = request.session.get('uid')
    user = User.objects.get(id=uid)
    
    # Get the user's last order, if it exists
    last_order = OrderYolzar.objects.filter(user=user).order_by('-order_date').first()

    # Check agar  user has any items in their resp cart
    cl = Cart.objects.filter(user=user)

    # Pre-fill the form with existing order details or render empty fields
    if last_order:
        initial_data = {
            'fname': last_order.fname,
            'lname': last_order.lname,
            'country': last_order.country,
            'address': last_order.address,
            'town_city': last_order.town_city,
            'country_state': last_order.country_state,
            'postcode': last_order.postcode,
            'phone': last_order.phone,
            'email': last_order.email,
            'accountpassword': last_order.accountpassword,
            'suggestions': last_order.suggestions,
        }
    else:
        initial_data = {}

    context = {
        'cl': cl,
        'initial_data': initial_data
    }

    return render(request, "checkout.html", context)




# def order_view(request):
#     if request.method == 'POST':
#         fname = request.POST.get('fname')
#         lname= request.POST.get('lname')
#         country =request.POST.get('country')
#         address =request.POST.get('address')
#         town_city = request.POST.get('town_city')
#         country_state =request.POST.get('country_state')
#         postcode = request.POST.get('postcode')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         accountpassword =request.POST.get('accountpassword')
#         suggestions = request.POST.get('suggestions')
#         order_date = request.POST.get('order_date')

#         order= OrderYolzar()
#         order.fname = fname
#         order.lname = lname
#         order.country = country
#         order.address = address
#         order.town_city = town_city
#         order.country_state = country_state
#         order.postcode = postcode
#         order.phone = phone
#         order.email  = email
#         order.accountpassword = accountpassword
#         order.suggestions = suggestions
#         order.order_date= order_date
#         order.save()
#         messages.success(request,'Address saved')
#         return redirect('/payment')

# def order_view(request):
#     if request.method == 'POST':
#         # Capture order details from the form
#         fname = request.POST.get('fname')
#         lname= request.POST.get('lname')
#         country =request.POST.get('country')
#         address =request.POST.get('address')
#         town_city = request.POST.get('town_city')
#         country_state =request.POST.get('country_state')
#         postcode = request.POST.get('postcode')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         accountpassword =request.POST.get('accountpassword')
#         suggestions = request.POST.get('suggestions')
#         total_amount = request.POST.get('total_amount')  # Capture the total amount
#         user = request.user

#         # Save order details to the database
#         order = OrderYolzar(
#             fname=fname,
#             lname=lname,
#             country=country,
#             address=address,
#             town_city=town_city,
#             country_state=country_state,
#             postcode=postcode,
#             phone=phone,
#             email=email,
#             accountpassword=accountpassword,
#             suggestions=suggestions,
#             user=user
#         )
#         order.save()

#         # Store the total amount in the session for use in the payment page
#         request.session['total_amount'] = total_amount
#         request.session['order_id'] = order.id  # Save the order ID

#         messages.success(request, 'Address saved')
#         return redirect('/payment')

def order_view(request):
    if request.method == 'POST':
        # Capture order details from the form
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        country = request.POST.get('country')
        address = request.POST.get('address')
        town_city = request.POST.get('town_city')
        country_state = request.POST.get('country_state')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        accountpassword = request.POST.get('accountpassword')
        suggestions = request.POST.get('suggestions')
        total_amount = request.POST.get('total_amount')  # Capture the total amount

        # Save order details to the database
        order = OrderYolzar(
            fname=fname,
            lname=lname,
            country=country,
            address=address,
            town_city=town_city,
            country_state=country_state,
            postcode=postcode,
            phone=phone,
            email=email,
            accountpassword=accountpassword,
            suggestions=suggestions,
            user=request.user  # Associate the order with the logged-in user
        )
        order.save()

        # Store the total amount and order ID in the session
        request.session['total_amount'] = total_amount
        request.session['order_id'] = order.id  # Save the order ID

        messages.success(request, 'Address saved successfully! Proceed to payment.')
        return redirect('/payment')  # Redirect to the payment page
    

# profile 

# def profile_view(request):
#     # yourdata = User.objects.all()
#     address = OrderYolzar.objects.all()
#     context  = {
#         'address':address
#     }
#     return render(request,'profile.html' , context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import OrderYolzar
from .forms import AddressForm
# def profile_view(request):
#     user = request.user
#     if request.method == 'POST':
#         form = AddressForm(request.POST)
#         if form.is_valid():
#             # Get or create the OrderYolzar instance for the user
#             order, created = OrderYolzar.objects.get_or_create(user=user)
#             # Update the OrderYolzar instance with the form data
#             form = AddressForm(request.POST, instance=order)
#             form.save()
#             messages.success(request, 'Address updated successfully!')
#             return redirect('profile')  # Redirect to the profile page after updating
#     else:
#         # Check if the user wants to edit their address
#         if request.GET.get('edit') == 'true':
#             order = OrderYolzar.objects.filter(user=user).first()
#             form = AddressForm(instance=order) if order else AddressForm()
#         else:
#             order = OrderYolzar.objects.filter(user=user).first()
#             form = AddressForm(instance=order) if order else AddressForm()

#     context = {
#         'form': form,
#         'is_edit': request.GET.get('edit') == 'true'
#     }
#     return render(request, 'profile.html', context)

def profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # Get or create the OrderYolzar instance for the user
            order, created = OrderYolzar.objects.get_or_create(user=user)
            # Update the OrderYolzar instance with the form data
            form = AddressForm(request.POST, instance=order)
            form.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('profile')  # Redirect to the profile page after updating
    else:
        # Check if the user wants to edit their address
        if request.GET.get('edit') == 'true':
            order = OrderYolzar.objects.filter(user=user).first()
            form = AddressForm(instance=order) if order else AddressForm()
        else:
            order = OrderYolzar.objects.filter(user=user).first()
            form = AddressForm(instance=order) if order else AddressForm()

    # Fetch ordered products
    ordered_products = OrderItem.objects.filter(order__user=user)

    context = {
        
        'form': form,
        'is_edit': request.GET.get('edit') == 'true',
        'ordered_products': ordered_products
    }
    return render(request, 'profile.html', context)
    
def payment_view(request):
    return render(request,'payment.html')
        


# def paymentdone_view(request):
#     # Assuming you have the order information stored in the session or database
#     order = OrderYolzar.objects.last()  # Example: Get the last order

#     # Send email
#     send_mail(
#         subject='Order Confirmation',
#         message=f'Thank you for your order, {order.fname}! Your order has been placed successfully. Thank you for shopping from YOLZAR',
#         from_email='your_email@example.com',
#         recipient_list=[order.email],
#         fail_silently=False,
#     )
#     Cart.objects.filter(user=request.user).delete()

#     messages.success(request, 'Order placed successfully! A confirmation email has been sent. ')
#     return redirect('/orderconfirm')  # Redirect to a confirmation page or wherever appropriate


def paymentdone_view(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = get_object_or_404(OrderYolzar, id=order_id)

        # Create OrderItem entries for each item in the cart
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.Product,
                quantity=item.quantity,
                
            )

        # Clear the cart
        cart_items.delete()

        # Send confirmation email
        send_mail(
            subject='Order Confirmation',
            message=f'Thank you for your order, {order.fname}! Your order has been placed successfully. Thank you for shopping with us.',
            from_email='your_email@example.com',
            recipient_list=[order.email],
            fail_silently=False,
        )

        # Display a success message
        messages.success(request, 'Order placed successfully! A confirmation email has been sent.')

    # Redirect to the order confirmation page
    return redirect('/orderconfirm')


def orderconfirm_view(request):
    return render(request,'orderconfirm.html')



#=============================================================================

import paypalrestsdk
from django.conf import settings
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages

import paypalrestsdk
from django.conf import settings

# Configure PayPal SDK
paypalrestsdk.configure({
    'mode': settings.PAYPAL_MODE,  # 'sandbox' or 'live'
    'client_id': settings.PAYPAL_CLIENT_ID,
    'client_secret': settings.PAYPAL_CLIENT_SECRET
})

def paypal_payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        
        if not amount:
            messages.error(request, 'Amount not provided. Please try again.')
            return redirect('/payment/')
        
        try:
            amount = "{:.2f}".format(float(amount))
        except ValueError:
            messages.error(request, 'Invalid amount format.')
            return redirect('/payment/')

        # PayPal payment creation logic
        payment = paypalrestsdk.Payment({
            'intent': 'sale',
            'payer': {'payment_method': 'paypal'},
            'redirect_urls': {
                'return_url': request.build_absolute_uri('/paypal/execute/'),
                'cancel_url': request.build_absolute_uri('/payment/')
            },
            'transactions': [{
                'item_list': {
                    'items': [{
                        'name': 'Order',
                        'sku': 'order',
                        'price': amount,
                        'currency': 'USD',
                        'quantity': 1
                    }]
                },
                'amount': {'total': amount, 'currency': 'USD'},
                'description': 'Order payment'
            }]
        })

        if payment.create():
            for link in payment.links:
                if (link.rel == 'approval_url'):
                    return redirect(link.href)
        else:
            messages.error(request, 'Payment creation failed. Please try again.')
            return redirect('/payment/')


def paypal_execute_view(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({'payer_id': payer_id}):
        # Payment successful, handle order creation
        order_id = request.session.get('order_id')
        order = get_object_or_404(OrderYolzar, id=order_id)

        # Create OrderItem entries for each item in the cart
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.Product,
                quantity=item.quantity
            )

        # Clear the cart after creating the order items
        cart_items.delete()

        # Send confirmation email
        send_mail(
            subject='Order Confirmation',
            message=f'Thank you for your order, {order.fname}! Your order has been placed successfully. Thank you for shopping from YOLZAR',
            from_email='your_email@example.com',
            recipient_list=[order.email],
            fail_silently=False,
        )

        messages.success(request, 'Order placed successfully! A confirmation email has been sent.')
        return redirect('/orderconfirm')
    else:
        messages.error(request, 'Payment execution failed.')
        return redirect('/payment/')
    


