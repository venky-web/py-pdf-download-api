from rest_framework import serializers
from api import models

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report_Page
        fields = '__all__'

class FeaturePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report_Feature_Page
        fields = '__all__'

class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Widget
        fields = '__all__'

