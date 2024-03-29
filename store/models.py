from autoslug.fields import AutoSlugField
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Sum
from django.urls import reverse
from ordered_model.models import OrderedModel

from users.models import User

from .managers import ProductQuerySet


class AbstractNamedModel(OrderedModel):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=150)
    slug = AutoSlugField(
        max_length=100, unique=True, populate_from="name", db_index=True
    )

    class Meta:
        abstract = True
        ordering = ["order"]


class Category(AbstractNamedModel):
    # TODO: add default
    img = models.ImageField(blank=True, upload_to="category")

    class Meta:
        ordering = ["order"]
        indexes = [
            models.Index(fields=["order"]),
        ]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Color(AbstractNamedModel):
    code = ColorField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "colors"


class Size(AbstractNamedModel):
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "sizes"


class Product(AbstractNamedModel):
    objects: ProductQuerySet = ProductQuerySet.as_manager()

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    describtion = models.TextField(max_length=1000)
    describtion_ar = models.TextField(max_length=1000)

    available = models.BooleanField(default=True)

    available_colors = models.ManyToManyField(
        Color, related_name="products", blank=True
    )
    available_sizes = models.ManyToManyField(Size, related_name="products", blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    related_products = models.ManyToManyField(
        "Product", related_name="parents", blank=True
    )

    visits = models.PositiveIntegerField(default=0)
    is_popular = models.BooleanField(default=False)

    price = models.FloatField(
        validators=[
            MinValueValidator(1, "Can't set price less than 1"),
            MaxValueValidator(100000, "Can't set price more than 100000"),
        ]
    )
    discount = models.FloatField(
        validators=[
            MaxValueValidator(100, "Can't make discount more than 100%"),
            MinValueValidator(0, "Can't create offer less than 0%"),
        ],
        default=0,
    )

    order_with_respect_to = "category"
    
    @property
    def price_after_discount(self):
        return self.price - (self.price * self.discount / 100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"slug": self.slug})


class ProductImage(OrderedModel):
    img = models.ImageField(upload_to="products")
    # TODO: add default
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


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey("store.Color", on_delete=models.CASCADE)
    size = models.ForeignKey("store.Size", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ["user", "product", "color", "size"]
        
class Order(models.Model):
    address = models.ForeignKey("users.BillingAddress", on_delete=models.CASCADE)
    alt_phone = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    notes = models.CharField(max_length=150, blank=True, null=True)

    class PaymentChoices(models.TextChoices):
        CASH_ON_DELIVERY = "cash_on_delivery", "Cash on delivery"
        ONLINE_PAYMENT = "online_payment", "Online Payment"

    payment_method = models.CharField(max_length=150, choices=PaymentChoices.choices)

    class StatusChoices(models.TextChoices):
        # online: unpaid -> paid -> delivered / canceled -> pending_refund -> refunded
        # cash: unpaid -> pending -> delivered / canceled -> pending_refund -> refunded
        UNPAID = "unpaid", "Unpaid"
        PAID = "paid", "Paid"
        PENDING = "pending", "Pending"
        CANCELED = "canceled", "Canceled"
        PENDING_REFUND = "pending_refund", "Pending refund"
        REFUNDED = "refunded", "Refunded"
        DELIVERED = "delivered", "Delivered"

    status = models.CharField(max_length=150, choices=StatusChoices.choices)

    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]

    @property
    def count(self):
        return self.items.aggregate(count=Sum("quantity"))

    @property
    def total(self):
        res = sum(item.get_cost() for item in self.items.all())
        # TODO convert to databse calculation
        # res = self.items.annotate(cost=F("price") * F("quantity")).aggregate(total=Sum('cost'))

        if self.fast_delivery:
            res += 15

        return res

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.id)
