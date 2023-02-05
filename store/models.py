from django.db import models
from autoslug.fields import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator
from ordered_model.models import OrderedModel
from django.contrib.auth import get_user_model
from django.db.models import Sum


class Category(OrderedModel):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=150)
    slug = AutoSlugField(max_length=100, unique=True, populate_from="name")
    img = models.ImageField(blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Product(OrderedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')

    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=150)

    slug = AutoSlugField(
        max_length=100, unique=True, populate_from="name", db_index=True
    )
    
    describtion = models.TextField(max_length=1000)
    describtion_ar = models.TextField(max_length=1000)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    related_products = models.ManyToManyField(
        "Product", related_name="parents", blank=True
    )
    
    visits = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["-created","order"]
        

    def __str__(self):
        return self.name
    
    
class Option(OrderedModel):
    name = models.CharField(max_length=150)
    name_ar = models.CharField(max_length=150)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="options"
    )
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    discount = models.FloatField(
        validators=[
            MaxValueValidator(100, "Can't make discount more than 100%"),
            MinValueValidator(0, "Can't create offer less than 0%"),
        ],
        default=0,
    )

    order_with_respect_to = "product"
    
    def __str__(self) -> str:
        return f"{self.product.name} | {self.name}"

    @property
    def price_after_discount(self):
        return self.price - (self.price * (self.discount / 100))



class ProductImage(OrderedModel):
    img = models.ImageField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )



class ProductReview(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(
        validators=[MaxValueValidator(5, "Can't rate product with more than 5 starts")]
    )
    comment = models.TextField()

    class Meta:
        unique_together = ["user", "product"]



class Order(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    alt_phone = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    street_number = models.CharField(max_length=20, null=True, blank=True)
    zone_number = models.CharField(max_length=20, null=True, blank=True)
    building_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=150,blank=True,null=True)
    fast_delivery = models.BooleanField(default=False)

    class PaymentChoices(models.TextChoices):
        CASH_ON_DELIVERY = "cash_on_delivery", "Cash on delivery"
        ONLINE_PAYMENT = "online_payment", "Online Payment"

    payment_method = models.CharField(
        max_length=150, choices=PaymentChoices.choices, default="cash_on_delivery"
    )

    class StatusChoices(models.TextChoices):
        UNPAID = "unpaid", "Unpaid"
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        CANCELED = "canceled", "Canceled"
        PENDING_REFUND = "pernding_refund", "Pending refund"
        REFUNDED = "refunded", "Refunded"
        DELIVERED = "delivered", "Delivered"

    status = models.CharField(
        max_length=150, choices=StatusChoices.choices, default=StatusChoices.UNPAID
    )

    class Meta:
        ordering = ["-created"]
        
    
    @property
    def count(self):
        return self.items.aggregate(count=Sum('quantity'))
    

    @property
    def total(self):
        res =  sum(
            item.get_cost() for item in self.items.all()
        )  
        # TODO convert to databse calculation
        # res = self.items.annotate(cost=F("price") * F("quantity")).aggregate(total=Sum('cost'))
        
        if self.fast_delivery:
            res += 15
            
        return res

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    option = models.ForeignKey(
        Option, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)



class Popular_Products(OrderedModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='popular_products')
    
    def __str__(self) -> str:
        return self.product.name