from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^laptops$', display_laptops, name="display_laptops"),
    url(r'^desktops$', display_desktops, name="display_desktops"),
    url(r'^mobiles$', display_mobiles, name="display_mobiles"),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),
    url(r'^add_mobile$', add_mobile, name='add_mobile'),

    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name="edit_laptop"),
    url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name="edit_desktop"),
    url(r'^edit_mobile/(?P<pk>\d+)$', edit_mobile, name="edit_mobile"),

]