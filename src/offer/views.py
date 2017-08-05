from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from query.models import Query


class Offer(LoginRequiredMixin, generic.ListView):
    model = Query
    paginate_by = 10
    context_object_name = "queries"
    template_name = "offer/offer.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return super(Offer, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(Offer, self).get_queryset().order_by('-id')