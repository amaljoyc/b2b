from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic


class Tender(LoginRequiredMixin, generic.TemplateView):
    template_name = "tender/tender.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(Tender, self).get(request, *args, **kwargs)