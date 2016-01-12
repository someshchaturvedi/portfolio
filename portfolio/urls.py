from django.conf.urls import include, url
import portfolio.views as views

urlpatterns = [
	url(r'^$' , views.index),
]