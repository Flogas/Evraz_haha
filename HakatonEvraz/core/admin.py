from django.contrib import admin
from .models import *
# Register your models here.


class ExhausterAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp']


admin.site.register(Exhauster, ExhausterAdmin)
admin.site.register(Bearing)
admin.site.register(BearingExtended)
admin.site.register(Cooler)
