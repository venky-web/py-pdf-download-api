from django.urls import path
from api import views

urlpatterns = [
    path('reports/', views.get_report, name='get_report'),
    path('pages/', views.get_page, name='get_page'),
    path('generate-pdf/', views.getData),
    path('delete-reports/', views.DeleteReports),
    path('delete-pages/', views.DeletePages),
    path('delete-feature-pages/', views.DeleteFeaturePages),
]