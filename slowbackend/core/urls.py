from django.urls import path

from .views import api_service_status_view


app_name = 'core'

urlpatterns = [
    path('service/status/', api_service_status_view, name='api_service_status'),
]
