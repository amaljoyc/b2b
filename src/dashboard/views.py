from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class ShowDashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/dashboard.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(ShowDashboard, self).get(request, *args, **kwargs)
