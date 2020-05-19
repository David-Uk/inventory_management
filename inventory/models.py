from django.db import models

# Create your models here.


class Device(models.Model):
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    choices = {
        ('AVAILABLE', 'Item ready for purchase'),
        ('SOLD', 'Item sold'),
        ('RESTOCKING', 'Item restocked soon')
    }
    status = models.CharField(max_length=10, default='SOLD')
    issues = models.CharField(max_length=100, default='No issues')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price :{1}'.format(self.type, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
