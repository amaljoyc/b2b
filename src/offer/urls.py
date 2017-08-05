from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^queries$', views.QueryList.as_view(), name='list_queries'),
    url(r'^do$', views.DoOffer.as_view(), name='do_offer'),
]
