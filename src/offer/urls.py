from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^do$', views.DoOffer.as_view(), name='do_offer'),
    url(r'^details$', views.OfferDetails.as_view(), name='show_details'),
    url(r'^accept$', views.DoAcceptOffer.as_view(), name='do_accept'),
]
