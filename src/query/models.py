from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField("Category", max_length=100)

    def __str__(self):
        return self.name

class BaseQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category)
    subject = models.CharField("Subject", max_length=500)
    content = models.TextField("Content")
    creation_date = models.DateTimeField("Creation Date", default=now)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Query(BaseQuery):
    def __str__(self):
        return "{}'s query". format(self.user)