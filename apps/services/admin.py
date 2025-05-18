from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Service Section', {
            'fields': ['Select_Service', 'description'],
            'description': 'The service section is for selecting a service from the list of services provided.'
        }),
        ('Others Section', {
            'fields': ['Others','Other_description','Othericon'],
            'description': 'The others section is for providing a custom service. If you select others, then the other fields will be required.'
        }),
    ]
    list_display = ('Select_Service', 'Others', 'Other_description', 'Othericon')
    
