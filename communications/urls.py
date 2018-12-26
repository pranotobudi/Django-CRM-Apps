from django.urls import re_path, path
from contacts.views import contact_detail, contact_cru
from .views import comm_detail

comm_urls = [
    re_path(r'^$',comm_detail, name="comm_detail"),

]
