from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Query.as_view(), name='query'),
    url(r'^queries$', views.QueryList.as_view(), name='list_queries'),
    url(r'^details$', views.QueryDetails.as_view(), name='show_details'),
]
