from django.contrib import admin

from accounts.models import Shopper
from store.models import Order,Cart

# Register your models here.
admin.site.register(Shopper)
admin.site.register(Order)
admin.site.register(Cart)