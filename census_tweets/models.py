# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import us
from django.db import models



class Tweet(models.Model):
    """
    Every tweet by @everytract.
    """
    id = models.CharField(max_length=500, unique=True, primary_key=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return 'https://twitter.com/everytract/status/{}/'.format(self.id)

    @property
    def tract(self):
        return self.text.split(",")[0].split()[-1].replace(".", "")

    @property
    def county(self):
        return self.text.split(",")[1]

    @property
    def state(self):
        return us.states.lookup(self.text.split()[-2])

    @property
    def state_fips(self):
        return us.states.lookup(self.text.split()[-2]).fips
