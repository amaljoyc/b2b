from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models


class Query(LoginRequiredMixin, generic.TemplateView):
    template_name = "query/query.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        kwargs["query_form"] = forms.QueryForm()
        return super(Query, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        query_form = forms.QueryForm(request.POST)
        if not (query_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                                    "Please check the details.")
            query_form = forms.QueryForm()
            return super(Query, self).get(request, query_form=query_form)

        query = query_form.save(commit=False)
        query.user = user
        query.save()

        messages.success(request, "Query saved!")
        return redirect("query:query")
