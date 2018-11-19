from django.conf.urls import url

from . import views
urlpatterns = [
	url(r'^masterdata_carwale/', views.masterdata_carwale, name='masterdata_carwale'),
	url(r'^carwale_scrap/', views.carwale_scrap, name='carwale_scrap'),
	url(r'^master_cartrade/', views.masterdata_cartrade, name='masterdata_cartrade'),
	url(r'^cartrade_scrap/', views.cartrade_scrap, name='cartrade_scrap'),
	url(r'^search/', views.store_scrapdata, name='search'),
	]