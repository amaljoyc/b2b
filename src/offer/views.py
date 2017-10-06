from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic
from query.models import Query

from . import forms
from .models import Offer


class DoOffer(LoginRequiredMixin, generic.TemplateView):
    template_name = "offer/offer.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        kwargs['query_id'] = request.GET.get('query')
        kwargs["offer_form"] = forms.OfferForm()
        return super(DoOffer, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        query_id = request.POST['query_id']
        offer_form = forms.OfferForm(request.POST)
        if not (offer_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                                    "Please check the details.")
            offer_form = forms.OfferForm()
            return super(DoOffer, self).get(request, offer_form=offer_form)

        offer = offer_form.save(commit=False)
        offer.user = user
        offer.query = Query.objects.get(id=query_id)
        offer.save()

        messages.success(request, "Offer saved!")
        return redirect("offer:do_offer")


class OfferDetails(LoginRequiredMixin, generic.TemplateView):
    template_name = "offer/offer_details.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        offer_id = request.GET.get('id')
        kwargs["offer"] = Offer.objects.get(id=offer_id)
        kwargs["request_user_id"] = self.request.user.id
        return super(OfferDetails, self).get(request, *args, **kwargs)

class DoAcceptOffer(LoginRequiredMixin, generic.TemplateView):
    template_name = "offer/accept.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        offer_id = request.GET.get('offer')
        offer = Offer.objects.get(id=offer_id)
        offer.accepted = True
        offer.save()
        return super(DoAcceptOffer, self).get(request, *args, **kwargs)