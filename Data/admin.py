# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Awards)
admin.site.register(Workshop)
admin.site.register(Event)
admin.site.register(Members)
admin.site.register(Home)