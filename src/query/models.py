from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings


class BaseQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.CharField("Category", max_length=100)
    content = models.TextField("Content")

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Query(BaseQuery):
    def __str__(self):
        return "{}'s query". format(self.user)
