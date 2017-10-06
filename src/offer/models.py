from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.timezone import now
from query.models import Query


class Offer(models.Model):
    creation_date = models.DateTimeField("Creation Date", default=now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    query = models.ForeignKey(Query)
    content = models.TextField("Offer Content")
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return "{}'s offer for query {}".format(self.user, self.query)