from django.contrib import admin
from .models import XrayReport,patient

# Register your models here.
class AdminPatient(admin.ModelAdmin):
    list_display=['id','name','phone','report']
admin.site.register(patient,AdminPatient)
admin.site.register(XrayReport)
