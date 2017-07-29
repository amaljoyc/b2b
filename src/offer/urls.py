from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Offer.as_view(), name='offer')
]
