import time

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

API_SERVICE_STATUS_OK = 'ok'


def api_service_status_view(request):
    a = [1 for _ in range(10000)]

    for _ in range(5000):
        for i in range(len(a)):
            a[i] += 1

    # time.sleep(settings.API_DELAY)

    return JsonResponse({'status': 200, 'message': API_SERVICE_STATUS_OK})
