from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from .views import custom_404_view, custom_500_view, custom_403_view, custom_400_view
from django.http import HttpResponse  
import datetime

def health_check(request):  
    print(f"[Health Check] Ping at {datetime.datetime.now()}")
    return HttpResponse("OK", status=200)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("branding.urls")),
    path("apps/contact/", include("apps.contact.urls")),
    path("apps/skills/", include("apps.skills.urls")),
    path("apps/work_experience/", include("apps.work_experience.urls")),
    path("apps/projects/", include("apps.projects.urls", namespace="projects")),
    path("apps/services/", include("apps.services.urls")),
    path("apps/education/", include("apps.education.urls")),
    path("apps/github/", include("apps.github.urls")),
    path("apps/tracking/", include("apps.tracking.urls")),
    path("device-charts/", include("apps.tracking.urls")),  # instead of apps/tracking/
    path("", include("apps.tracking.urls")),
    


    path("health/", health_check),
]

# Serve media files correctly
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#     ]
# Serve static files correctly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]


# Global error handlers
handler404 = custom_404_view 
handler500 = custom_500_view
handler403 = custom_403_view
handler400 = custom_400_view
