from django.db import models
from autoslug.fields import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator
from ordered_model.models import OrderedModel


class Category(OrderedModel):
    name = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=150)
    slug = AutoSlugField(max_length=100, unique=True, populate_from="name")
    img = models.ImageField(blank=True)

    class Meta:
        ordering = ["order"]
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
        ordering = ["order"]
        

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
