import twitter
from pprint import pprint
from django.conf import settings
from census_tweets.models import Tweet
from dateutil.parser import parse as dateparse
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Download tweets from @everytract"

    def handle(self, *args, **options):

        api = twitter.Api(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )
        statuses = api.GetUserTimeline(screen_name="@everytract")
        for s in statuses:
            obj, c = Tweet.objects.get_or_create(
                id=s.id,
                text=s.text,
                created_at=dateparse(s.created_at)
            )
            if c:
                print("Created {}".format(obj))
