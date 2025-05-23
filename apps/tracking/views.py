import csv
import json
from collections import Counter
from datetime import datetime
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.html import format_html
from django.views.decorators.csrf import csrf_exempt
from .models import DeviceLog


# ======================
# Views
# ======================
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

@csrf_exempt
def log_device_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            device = data.get('device', 'Unknown')
            brand = data.get('brand', 'Unknown')
            dtype = data.get('type', 'Unknown')
            os = data.get('os', 'Unknown')
            browser = data.get('browser', 'Unknown')
            ip = get_client_ip(request)

            DeviceLog.objects.create(
                ip_address=ip,
                brand=brand,
                device=device,
                device_type=dtype,
                os=os,
                browser=browser
            )

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@staff_member_required
def device_charts(request):
    logs = DeviceLog.objects.all()

    os_counts = Counter([log.os for log in logs])
    browser_counts = Counter([log.browser for log in logs])
    type_counts = Counter([log.device_type for log in logs])

    context = {
        "os_data": json.dumps(os_counts),
        "browser_data": json.dumps(browser_counts),
        "type_data": json.dumps(type_counts)
    }
    return render(request, "tracking/device_charts.html", context)
