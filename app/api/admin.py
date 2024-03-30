"""
Django admin customization.
"""
from django.contrib import admin

from api import models

admin.site.register(models.Report)
admin.site.register(models.Report_Page)
admin.site.register(models.Report_Feature_Page)
admin.site.register(models.Page_Widget_Mapping)
admin.site.register(models.Widget)
