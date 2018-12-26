from django.urls import re_path, path
from contacts.views import contact_detail
contact_urls = [
    re_path(r'^$', contact_detail, name="contact_detail"),

]
