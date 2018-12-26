from django.urls import re_path, path
from contacts.views import contact_detail, contact_cru
contact_urls = [
    re_path(r'^$', contact_detail, name="contact_detail"),
    re_path(r'^edit/$',contact_cru, name='contact_update'),

]
