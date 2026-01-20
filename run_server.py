#!/usr/bin/env python
"""
Django Inventory Management Server Launcher
This script sets up the Django environment and runs the development server.
"""

import os
import sys
import subprocess
import django
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()
os.chdir(PROJECT_ROOT)

# Add project to path
sys.path.insert(0, str(PROJECT_ROOT))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AUtomation_inventory_management.settings')
django.setup()

# Run migrations
print("=" * 60)
print("Running database migrations...")
print("=" * 60)
subprocess.run([sys.executable, 'manage.py', 'migrate'], check=False)

print("\n" + "=" * 60)
print("Starting Django Development Server")
print("=" * 60)
print("Opening server at http://127.0.0.1:8000/")
print("Press Ctrl+C to stop the server")
print("=" * 60 + "\n")

# Run the development server
subprocess.run([sys.executable, 'manage.py', 'runserver'], check=False)
