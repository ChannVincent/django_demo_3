from django.contrib import admin
from .models import Enterprise, Share, Dividend, Badge

admin.site.register(Enterprise)
admin.site.register(Share)
admin.site.register(Dividend)
admin.site.register(Badge)