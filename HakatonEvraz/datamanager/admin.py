from django.contrib import admin
from .models import *
# Register your models here.


class ExhausterAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(ExhausterObj, ExhausterAdmin)
admin.site.register(BearingObj)
admin.site.register(BearingExtendedObj)
admin.site.register(CoolerObj)
