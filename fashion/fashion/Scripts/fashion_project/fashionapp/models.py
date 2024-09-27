from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    class Meta:
        db_table = 'category'
    def __str__(self):
        return self.category_name

class Product (models.Model):
    p_img1 = models.ImageField(default='',upload_to="image")
    p_img2 = models.ImageField(default='',upload_to="image")
    p_img3 = models.ImageField(default='',upload_to="image")
    p_name = models.CharField(max_length=30)
    p_price = models.IntegerField()
    p_description = models.TextField(max_length=300)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name

    class Meta:
        db_table = 'product'


# class Cart(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     Product = models.ForeignKey(Product,on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'cart'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.Product.p_name} - {self.user.username}"
    
    class Meta:
        db_table = 'cart'

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'


# class OrderYolzar(models.Model):
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     country = models.CharField(max_length=30)
#     address = models.CharField(max_length=30)
#     town_city = models.CharField(max_length=30)
#     country_state = models.CharField(max_length=30)
#     postcode = models.CharField(max_length=30)
#     phone = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     accountpassword = models.TextField(max_length=300)
#     suggestions = models.CharField(max_length=30)
#     order_date = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         db_table = "orderY"

#     def __str__(self):
#         return f'Order by {self.fname} {self.lname}'
class OrderYolzar(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    town_city = models.CharField(max_length=30)
    country_state = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    accountpassword = models.TextField(max_length=300)
    suggestions = models.CharField(max_length=30)
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)  # Add this line
    
    class Meta:
        db_table = "orderY"

    def __str__(self):
        return f'Order by {self.fname} {self.lname}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(OrderYolzar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
   

    def __str__(self):
        return f'{self.quantity} x {self.product.p_name}'



class PayPalTransaction(models.Model):
    order = models.ForeignKey('OrderYolzar', on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, unique=True)
    payer_email = models.EmailField()
    payment_status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.payment_status}"