from django.conf import settings
from django.db import models


class ItemTag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=70)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    clicks = models.IntegerField(default=0)
    tags = models.ForeignKey(ItemTag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} @ {1}'.format(self.product.name,
                                  self.product.price)


class Order(models.Model):
    STATUS = (
        ('requested', 'Requested'),
        ('pending', 'Pending'),
        ('finished', 'Finished'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_status = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='requested', max_length=10)

    def __str__(self):
        return self.user.username
