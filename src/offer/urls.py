from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^do$', views.DoOffer.as_view(), name='do_offer'),
]
