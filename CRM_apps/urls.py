"""CRM_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from marketing.views import HomePage
from subscribers.views import subscriber_new
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import AccountList, account_cru
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import contact_cru
from contacts.views import ContactDelete
from communications.urls import comm_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('signup/',subscriber_new, name='sub_new'),
    path('login/',
        LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path('logout/',
        LogoutView.as_view(next_page='/login/')
    ),
    re_path(r'^account/new/$',
        account_cru, name='account_new'
    ),
    re_path(r'^account/list/$',
        AccountList.as_view(), name='account_list'
    ),
    #re_path(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
    re_path(r'^account/(?P<uuid>\w+)/', include(account_urls)),
    #re_path(r'^account/(?P<uuid>)/', include(account_urls)),
    re_path(r'^contact/new/$',contact_cru, name='contact_new'),
    re_path(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
    re_path(r'^contact/(?P<pk>[\w-]+)/delete/$',
    ContactDelete.as_view(), name='contact_delete'),
    re_path(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),


]
