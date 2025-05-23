from django.db import models

# ======================
# DeviceLog Model
# ======================
from django.db import models

class DeviceLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    brand = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    os = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.timestamp} - {self.device} ({self.ip_address})"
