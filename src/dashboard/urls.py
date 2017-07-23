from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ShowDashboard.as_view(), name='show_dashboard')
]
