"""
Database models.
"""
from django.conf import settings
from django.db import models


class Report(models.Model):
    """Report object."""
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    report_id = models.CharField(max_length=50)
    report_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=500)
    created_by = models.IntegerField(null=True)
    created_dt = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    update_dt = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, blank=True)
    is_deleted = models.CharField(max_length=2, default='N')
    container_id = models.IntegerField()
    import_from_report_id = models.CharField(max_length=255)
    # tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.report_name
    

class Report_Page(models.Model):
    """Report page object"""
    page_id = models.CharField(max_length=100)
    report_id = models.CharField(max_length=100)
    page_name = models.CharField(max_length=100)
    page_order = models.IntegerField()
    status = models.CharField(max_length=20, blank=True)
    definition = models.JSONField(null=True)
    created_by = models.IntegerField(null=True)
    created_dt = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    update_dt = models.DateTimeField(null=True)

    def __str__(self):
        return self.page_name


class Report_Feature_Page(models.Model):
    """Report feature page object"""
    feature_page_id = models.CharField(max_length=100, primary_key=True)
    object_id = models.CharField(max_length=100)
    object_type = models.CharField(max_length=25)
    definition = models.JSONField()
    created_by = models.IntegerField(null=True)
    created_date = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateTimeField(null=True)
    container_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.object_type}_{self.object_id}"


class Page_Widget_Mapping(models.Model):
    """Model for page and widget mapping."""
    mapping_id = models.CharField(max_length=100, primary_key=True)
    page_id = models.CharField(max_length=100)
    widget_id = models.CharField(max_length=255)
    page_type = models.CharField(max_length=255)

    def __str__(self):
        return self.mapping_id


class Widget(models.Model):
    """Widget object"""
    widget_id = models.CharField(max_length=100, primary_key=True)
    widget_name = models.CharField(max_length=100)
    definition = models.JSONField()
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    container_id = models.IntegerField(null=True)
    is_shared = models.CharField(max_length=2)
    is_deleted = models.CharField(max_length=2)

    def __str__(self):
        return self.widget_name
