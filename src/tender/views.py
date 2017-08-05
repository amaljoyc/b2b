from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from query.models import Query


class Tender(LoginRequiredMixin, generic.ListView):
    model = Query
    paginate_by = 4
    context_object_name = "queries"
    template_name = "tender/tender.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(Tender, self).get(request, *args, **kwargs)