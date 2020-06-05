from django.conf import settings
from django.db import models
from django.shortcuts import reverse


STATUS = (
    ('requested', 'Requested'),
    ('pending', 'Pending'),
    ('finished', 'Finished')
)

TAG_COLOURS = (
    ('danger', 'Red'),
    ('success', 'Green'),
    ('info', 'Blue'),
    ('warning', 'Yellow'),
    ('secondary', 'Gray')
)


class ItemTag(models.Model):
    name = models.CharField(max_length=10)
    colour = models.CharField(choices=TAG_COLOURS,
                              max_length=10, default='Red')

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    description = models.TextField(max_length=70)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    clicks = models.IntegerField(default=0)
    tag = models.ForeignKey(
        ItemTag, null=True, blank=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('orders:product', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.name

    

    def get_add_to_cart_url(self):
        return reverse('orders:add_to_cart', kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(
          settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    # QUANTITY IS NOT NEEDED!!!!
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '{0} @ {1}'.format(self.item.name,
                                  self.item.price)


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        choices=STATUS, default='requested', max_length=10)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
