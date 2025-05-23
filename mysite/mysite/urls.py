"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.urls import re_path as url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.sitemaps.views import sitemap

from Bable.sitemaps import Static_Sitemap, Post_Sitemap, Anon_Sitemap

from django.views.generic import View
from django.http.response import HttpResponse
class Adsense(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('google.com, pub-3397601491384059, DIRECT, f08c47fec0942fa0', content_type="text/plain")
sitemaps = {
    'post': Post_Sitemap(),
    'static': Static_Sitemap(),
    'user': Anon_Sitemap(),
    
}


urlpatterns = [
	url(r'^paypal/', include('paypal.standard.ipn.urls')),
	path('B/', include('Bable.urls')),
    path('ads.txt', Adsense.as_view()),
    path('', RedirectView.as_view(pattern_name='Bable:landingpage')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
