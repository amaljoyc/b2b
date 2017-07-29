from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Tender.as_view(), name='tender')
]
