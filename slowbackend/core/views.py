import time

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

API_SERVICE_STATUS_OK = 'ok'


def api_service_status_view(request):
    time.sleep(settings.API_DELAY)
    return JsonResponse({'status': 200, 'message': API_SERVICE_STATUS_OK})
