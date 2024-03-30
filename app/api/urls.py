from django.urls import path
from api import views

urlpatterns = [
    path('', views.getData),
    path('delete-reports', views.DeleteReports),
    path('delete-pages', views.DeletePages),
    path('delete-feature-pages', views.DeleteFeaturePages),
]