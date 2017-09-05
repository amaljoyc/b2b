from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

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


class QueryList(LoginRequiredMixin, generic.ListView):
    model = models.Query
    paginate_by = 6
    context_object_name = "queries"
    template_name = "offer/query_list.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(QueryList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        cat = self.request.GET.get('cat')
        find = self.request.GET.get('find')
        if cat:
            return super(QueryList, self).get_queryset().order_by('-id').filter(category__name__icontains=cat)
        elif find:
            return super(QueryList, self).get_queryset().order_by('-id').\
                filter(Q(category__name__icontains=find) | Q(subject__icontains=find) | Q(content__icontains=find))
        else:
            return super(QueryList, self).get_queryset().order_by('-id')