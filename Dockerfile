# Use an official Python image
FROM python:3.11-slim

# Environment configs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations, create superuser, start Gunicorn
CMD sh -c "python manage.py migrate && \
           python manage.py createsuperuser --noinput || true && \
           python -c 'import os; import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username=os.environ[\"DJANGO_SUPERUSER_USERNAME\"]); user.set_password(os.environ[\"DJANGO_SUPERUSER_PASSWORD\"]); user.save()' && \
           gunicorn myproject.wsgi:application --workers=1 --bind 0.0.0.0:24875"

