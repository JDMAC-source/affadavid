# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User, UserManager
from django.db import models
# Register your models here.
class Anon(User):
	latest_change_date = models.DateTimeField(default=timezone.now)
	#playlists = models.ManyToManyField(Playlist)
	
	objects = UserManager()