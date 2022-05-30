from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

from users.models import User


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=64, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'Product categories'

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    size = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    category = TreeForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True)
    color = models.CharField(blank=True, max_length=32)
    brand = models.CharField(blank=True, max_length=64)
    specification = models.CharField(blank=True, max_length=128)
    published = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('shop-single', kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} | {self.category}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart for {self.user.username} | Product {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price




class RatingStar(models.Model):
    """Star of rating"""
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name_plural = 'Stars of rating'


class ProductImages(models.Model):
    """Personal product page images"""
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='product_images/')
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product images'


class Rating(models.Model):
    """Product rating"""
    ip = models.CharField('IP address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.product}'

    class Meta:
        verbose_name_plural = 'Ratings'


class Reviews(models.Model):
    """Product reviews"""
    name = models.CharField("Name", max_length=100)
    text = models.TextField('Text', max_length=5000)
    email = models.EmailField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name_plural = 'Reviews'
