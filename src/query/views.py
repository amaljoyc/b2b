from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views import generic
from offer.models import Offer

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
    paginate_by = 4
    context_object_name = "queries"
    template_name = "query/query_list.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(QueryList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        cat = self.request.GET.get('cat')
        find = self.request.GET.get('find')
        if cat:
            set = super(QueryList, self).get_queryset().order_by('-id').filter(category__name__icontains=cat)
        elif find:
            set = super(QueryList, self).get_queryset().order_by('-id').\
                filter(Q(category__name__icontains=find) | Q(subject__icontains=find) | Q(content__icontains=find))
        else:
            set = super(QueryList, self).get_queryset().order_by('-id')

        return set.exclude(user_id=self.request.user.id)


class QueryDetails(LoginRequiredMixin, generic.TemplateView):
    model = models.Query
    template_name = "query/query_details.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        query_id = request.GET.get('id')
        kwargs["query"] = models.Query.objects.get(id=query_id)
        kwargs["request_user_id"] = self.request.user.id
        return super(QueryDetails, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        query_id = self.request.GET.get('id')
        context = super(QueryDetails, self).get_context_data(**kwargs)
        context['offers'] = Offer.objects.filter(query_id=query_id).order_by('-id')
        return context