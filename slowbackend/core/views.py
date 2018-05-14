import time
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

API_SERVICE_STATUS_OK = 'ok'


def api_service_status_view(request):
    a = [1 for _ in range(10000)]

    for _ in range(25):
        for i in range(len(a)):
            a[i] += 1

    # time.sleep(settings.API_DELAY)

    return JsonResponse({'status': 200, 'message': API_SERVICE_STATUS_OK, 'method': 'service'})


def api_sample_load_view(request):
    def sample_primes(n):
        result = []
        for p in range(2, n + 1):
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                result.append(p)
        return result

    before = datetime.now()
    result = sample_primes(10000)
    elapsed = datetime.now() - before

    return JsonResponse({'status': 200, 'message': API_SERVICE_STATUS_OK, 
                         'method': 'load', 'result': result, 'elapsed_time': elapsed})
