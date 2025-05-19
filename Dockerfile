# 1. Use an official Python image from DockerHub
FROM python:3.11-slim

# 2. Set environment variables to prevent .pyc files and enable logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory in the container
WORKDIR /code

# 4. Copy only requirements first, and install them
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy the rest of the project files into the container
COPY . /code/

# 5.1 Install additional dependencies if needed
ENV DJANGO_SETTINGS_MODULE=portfolio.settings

# 6. Collect static files (for deployment)
RUN python manage.py collectstatic --noinput

# 7. Expose port 8000 (this is what Django runs on)
EXPOSE 8000

# 8. Start the Django app using Gunicorn (production-ready server)
CMD sh -c "python manage.py migrate && \
           python manage.py createsuperuser --noinput && \
           python -c 'import os; import django; django.setup(); from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username=os.environ[\"DJANGO_SUPERUSER_USERNAME\"]); user.set_password(os.environ[\"DJANGO_SUPERUSER_PASSWORD\"]); user.save()' && \
           gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT"



