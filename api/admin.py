from django.contrib import admin

# Register your models here.

from .models import Kompyuter,Smartphones

admin.site.register(Kompyuter)
admin.site.register(Smartphones)