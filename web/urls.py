"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.Register.as_view(), name='register'),
    path('paste', views.make_paste, name='make_paste'),
    path('<int:paste_id>', views.show_paste, name='show_paste'),
    path('<int:pk>/delete', views.PasteDelete.as_view(), name='delete_paste'),
    path('<int:pk>/edit', views.PasteUpdate.as_view(), name='edit_paste'),
    path('all', views.ListPastes.as_view(), name='all_pastes'),
    path('<int:paste_id>/raw', views.show_raw, name='show_raw'),
    path('stats', views.show_site_stats, name='show_site_stats'),
    path('my_pastes', views.ListMyPastes.as_view(), name='my_pastes'),
    path('privacy_policy', views.PrivacyPolicy.as_view(), name='privacy_policy'),
]
