# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "tract", "county", "state", "fips", "geoid", "census_url", "reply_id")
    search_fields = ("text",)
    date_hierarchy = "created_at"
    list_editable = ("reply_id",)
