from django.conf import settings
from django.db import models
from django.shortcuts import reverse


class ItemTag(models.Model):
    """
    A model for the item tags with selectable
    Bootstrap colours.
    """
    TAG_COLOURS = (
        ('danger', 'Red'),
        ('success', 'Green'),
        ('info', 'Blue'),
        ('warning', 'Yellow'),
        ('secondary', 'Gray')
    )

    name = models.CharField(max_length=10)
    colour = models.CharField(
        choices=TAG_COLOURS, max_length=10, default='Red')

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    A model for the items/products.
    Urls are slug based.
    """
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    description = models.TextField(max_length=70)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    clicks = models.IntegerField(default=0)
    tag = models.ForeignKey(
        ItemTag, null=True, blank=True, on_delete=models.SET_NULL)

    def get_add_to_cart_url(self):
        return reverse('orders:add_to_cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('orders:remove_from_cart', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    """
    A model for the order items
    to be collected by the order.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def get_total_item_price(self):
        return self.item.price

    def __str__(self):
        return self.item.name


class Order(models.Model):
    """
    A model to collect
    the order items in 1 order
    """
    STATUS = (
        ('requested', 'Requested'),
        ('pending', 'Pending'),
        ('finished', 'Finished')
    )

    id_code = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    status = models.CharField(
        choices=STATUS, default='requested', max_length=10)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    total = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    artwork = models.FileField(
        upload_to='artwork/%Y/%m/%d', blank=True, null=True)
    comments = models.TextField(max_length=250, blank=True, null=True)
    billing_address = models.ForeignKey(
        'checkout.BillingAddress',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    payment = models.ForeignKey(
        'checkout.Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def __str__(self):
        return self.user.username
