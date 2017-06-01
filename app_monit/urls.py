"""apimonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^twittermonitor.herokuapp.com/admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/twittermonitor.herokuapp.com/monitoramentos/', permanent=True)),
    url(r'^twittermonitor.herokuapp.com/accounts/', include('django.contrib.auth.urls')),
    url(r'^twittermonitor.herokuapp.com/', include('twitter_monitor.urls', namespace='monitoramento')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

