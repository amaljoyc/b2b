from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic


class Query(LoginRequiredMixin, generic.TemplateView):
    template_name = "query/query.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(Query, self).get(request, *args, **kwargs)