from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^laptops$', display_laptops, name="display_laptops"),
]
