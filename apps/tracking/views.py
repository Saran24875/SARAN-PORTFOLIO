import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DeviceLog
from datetime import datetime

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
