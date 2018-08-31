# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import us
import twitter
from django.db import models
from django.conf import settings
from census_tweets import lookup


class Tweet(models.Model):
    """
    Every tweet by @everytract.
    """
    # The @everytract tweet
    id = models.CharField(max_length=500, unique=True, primary_key=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField()

    # The @everytractcount reply
    reply_id = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.text

    @property
    def everytract_url(self):
        return 'https://twitter.com/everytract/status/{}/'.format(self.id)

    @property
    def census_url(self):
        return 'https://censusreporter.org/profiles/{}'.format(self.geoid)

    @property
    def tract(self):
        t = self.text.split(",")[0].split()[-1].strip()
        if "." not in t:
            t += ".00"
        i = int(t.replace(".", ""))
        return "{:06d}".format(i)

    @property
    def county(self):
        return self.text.split(",")[1].strip()

    @property
    def state(self):
        return us.states.lookup(self.text.split()[-2].strip())

    @property
    def fips(self):
        return lookup.county(self.state.abbr, self.county)

    @property
    def geoid(self):
        return '14000US{}{}'.format(self.fips, self.tract)

    def post_reply(self):
        if self.reply_id:
            return False
        api = twitter.Api(
            consumer_key=settings.TWITTER_WRITE_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_WRITE_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_WRITE_ACCESS_TOKEN_KEY,
            access_token_secret=settings.TWITTER_WRITE_ACCESS_TOKEN_SECRET
        )
        status = api.PostUpdate(self.census_url)
        self.reply_id = status.id
        self.save()
