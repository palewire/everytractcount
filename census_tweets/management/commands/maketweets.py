import time
from census_tweets.models import Tweet
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Make tweets at @everytract"

    def handle(self, *args, **options):
        for tweet in Tweet.objects.filter(reply_id=''):
            print(tweet)
            tweet.post_reply()
            time.sleep(3)
