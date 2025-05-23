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
# Admin
# ======================
@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address', 'brand', 'device', 'device_type', 'os', 'browser')
    search_fields = ('ip_address', 'brand', 'device', 'os', 'browser')
    list_filter = ('device_type', 'os', 'browser')
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="device_logs.csv"'
        writer = csv.writer(response)

        writer.writerow(['Timestamp', 'IP Address', 'Brand', 'Device', 'Type', 'OS', 'Browser'])
        for log in queryset:
            writer.writerow([
                log.timestamp,
                log.ip_address,
                log.brand,
                log.device,
                log.device_type,
                log.os,
                log.browser
            ])
        return response

    export_as_csv.short_description = "Export Selected Logs to CSV"

    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context['charts_url'] = reverse("device-charts")
        return super().changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
        return False
