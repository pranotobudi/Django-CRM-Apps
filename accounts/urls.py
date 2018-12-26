from django.urls import re_path, path
from .views import account_detail
account_urls = [
    re_path(r'^$',account_detail, name='account_detail'),
    #re_path(r'^$',AccountList.as_view(), name='account_detail'),
]
