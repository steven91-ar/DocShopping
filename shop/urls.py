from itertools import product

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from accounts.views import signup, logout_user, login_user
from store.views import index, product_detail

from shop import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add_to'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
