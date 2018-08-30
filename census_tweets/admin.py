# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "tract", "county", "state", "state_fips")
    search_fields = ("text",)
    date_hierarchy = "created_at"
