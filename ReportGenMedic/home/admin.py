from django.contrib import admin
from .models import XrayReport,Patient

# Register your models here.
class AdminPatient(admin.ModelAdmin):
    list_display=['username','name','phone','report']
admin.site.register(Patient,AdminPatient)
admin.site.register(XrayReport)
