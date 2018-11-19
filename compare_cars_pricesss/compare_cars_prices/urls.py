"""compare_cars_prices URL Configuration

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
# """
# from django.conf.urls import include, url
# from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from compare_cars.views import Get_allMakes,Get_allMakesDetails,Get_allModelDetails,Get_DataFromCity,Get_AllDataFromCity

admin.autodiscover()


urlpatterns = patterns(
    '',
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cars/', include('cars_scrapping.urls', namespace='cars')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/$', Get_allMakes.as_view(), name='api_list'),
    # url(r'^api/(?P<car_make>[A-Za-z0-9\w @%._-]+)/$',Get_allMakesDetails, name='api_detail'),
    url(r'^api/(?P<car_make>[A-Za-z0-9\w @%._-]+)/(?P<car_model>[A-Za-z0-9\w @%._-]+)/$',Get_allModelDetails, name='api_modeldetail'),
    url(r'^api/(?P<city>[A-Za-z0-9\w@%._-]+)/$', Get_DataFromCity, name='api_city'),
    url(r'^api/(?P<city>[A-Za-z0-9\w@%._-]+)/(?P<car_make>[A-Za-z0-9\w @%._-]+)/(?P<car_model>[A-Za-z0-9\w @%._-]+)/$',Get_AllDataFromCity, name='api_citydetail'),
    

 )

urlpatterns+=staticfiles_urlpatterns()

