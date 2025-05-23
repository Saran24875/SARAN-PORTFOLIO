from django.urls import path
from .views import log_device_info
from .admin_views import device_charts  # <- make sure this file exists

# ======================
# URLs
# ======================
urlpatterns = [
    path("log-device-info/", log_device_info, name="log-device-info"),
    path("tracking/device-charts/", device_charts, name="device-charts"),
]  # Make sure this is included from apps.tracking.urls in the main project urls.py
