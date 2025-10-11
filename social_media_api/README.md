# Social Media API Deployment Documentation

## Hosting Service
- Platform: Render
- URL: https://alx-djangolearnlab-1-wgrp.onrender.com

## Deployment Steps
1. Created a PostgreSQL database on Render.
2. Added environment variables:
   - SECRET_KEY
   - DEBUG
   - ALLOWED_HOSTS
   - DB_ENGINE
   - DB_NAME
   - DB_USER
   - DB_PASSWORD
   - DB_HOST
   - DB_PORT
3. Installed Gunicorn and configured the web service command:

gunicorn social_media_api.wsgi:application

4. Set `DEBUG=False` and updated `ALLOWED_HOSTS`.
5. Collected static files with:

python manage.py collectstatic

6. Verified successful deployment at Render.

## Monitoring & Maintenance
- Logs are monitored through Render’s dashboard.
- Future updates will involve CI/CD integration for smoother deployments.

