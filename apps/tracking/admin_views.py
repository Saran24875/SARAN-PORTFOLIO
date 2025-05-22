from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import DeviceLog
from collections import Counter
import json

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
    return render(request, "admin/tracking/device_charts.html", context)
