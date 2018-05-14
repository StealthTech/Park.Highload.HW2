from django.urls import path

from .views import api_service_status_view, api_sample_load_view


app_name = 'core'

urlpatterns = [
    path('service/status/', api_service_status_view, name='api_service_status'),
    path('service/sample/', api_sample_load_view, name='api_service_sample'),
]
