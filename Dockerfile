# 1. Use an official Python image from DockerHub
FROM python:3.11-slim

# 2. Set environment variables to prevent .pyc files and enable logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory in the container
WORKDIR /code

# 4. Copy only requirements first, and install them
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy the rest of the project files into the container
COPY . /code/

# 6. Collect static files (for deployment)
RUN python manage.py collectstatic --noinput

# 7. Expose port 8000 (this is what Django runs on)
EXPOSE 8000

# 8. Start the Django app using Gunicorn (production-ready server)
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
