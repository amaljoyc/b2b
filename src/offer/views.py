from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic


class Offer(LoginRequiredMixin, generic.TemplateView):
    template_name = "offer/offer.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(Offer, self).get(request, *args, **kwargs)