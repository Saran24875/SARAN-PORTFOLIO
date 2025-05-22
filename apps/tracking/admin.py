import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import DeviceLog

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

        # Write header
        writer.writerow(['Timestamp', 'IP Address', 'Brand', 'Device', 'Type', 'OS', 'Browser'])

        # Write data rows
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
