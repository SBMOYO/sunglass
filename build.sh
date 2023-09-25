#!/bin/sh

# Install dependencies:
pip install -r requirements.txt

# Collect static files:
python manage.py collectstatic --noinput

# Database migration 
python manage.py migrate