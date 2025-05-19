import os
import django

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.get(username=os.environ['DJANGO_SUPERUSER_USERNAME'])
user.set_password(os.environ['DJANGO_SUPERUSER_PASSWORD'])
user.save()
