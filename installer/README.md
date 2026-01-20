# Inventory Management System - Installer

## Quick Start

### Installation (First Time Only)

1. Open PowerShell or Command Prompt
2. Navigate to the project root directory
3. Run:
```bash
installer\install.bat
```

This will:
- ✅ Create a Python virtual environment
- ✅ Install all dependencies
- ✅ Run database migrations
- ✅ Create desktop shortcuts

### Running the Application

After installation, a shortcut will appear on your Desktop:

#### Option 1: Using Desktop Shortcut (Easiest)

1. **Double-click "Inventory Manager Server"** - Starts Django web server
2. Open browser to `http://localhost:8000/`

#### Option 2: Manual Start (From Command Prompt)

```bash
installer\run_server.bat
```

## Access Points

Once running, access the application at:

- **Dashboard**: http://localhost:8000/
- **Admin Panel**: http://localhost:8000/admin/
- **API**: http://localhost:8000/api/

## File Structure

```
installer/
├── install.bat                  # Main installer script
├── run_server.bat              # Start Django server
├── create_shortcuts.py         # Creates desktop shortcuts
└── README.md                   # This file
```

## Troubleshooting

### Python Not Found
- Make sure Python 3.8+ is installed
- Add Python to Windows PATH
- Restart Command Prompt after installing Python

### Virtual Environment Issues
```bash
# Manually create and activate:
python -m venv myenv
myenv\Scripts\activate.bat
pip install django lxml
```

### Manual Database Reset
```bash
myenv\Scripts\activate.bat
python manage.py migrate
```

### Manual Desktop Shortcut Creation
If automated shortcuts fail, create them manually:

1. Right-click Desktop → New → Shortcut
2. Location: `C:\path\to\project\installer\run_server.bat`
3. Name: `Inventory Manager Server`

## Default Credentials

To create a superuser/admin account:
```bash
myenv\Scripts\activate.bat
python manage.py createsuperuser
```

Then access admin at: http://localhost:8000/admin/

## Stopping the Application

- Press `Ctrl+C` in the command window
- Or close the command window directly

## Important Notes

⚠️ **Always keep the Django server running for full functionality**

The server window shows all activity and errors for debugging

---

**For Support or Issues, check the project logs!**
