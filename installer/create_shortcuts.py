"""
Create desktop shortcuts for Inventory Management application
Run as: python create_shortcuts.py <project_root>
"""
import sys
import os
import subprocess


def create_shortcut_with_powershell(project_root, shortcut_name, target_script, description):        
    """Create shortcut using PowerShell"""
    shortcut_path = os.path.expanduser(f"~\\Desktop\\{shortcut_name}.lnk")

    ps_script = f"""
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{target_script}"
$Shortcut.WorkingDirectory = "{project_root}"
$Shortcut.Description = "{description}"
$Shortcut.IconLocation = "C:\\Windows\\System32\\cmd.exe"
$Shortcut.Save()
"""

    try:
        subprocess.run(
            ["powershell", "-Command", ps_script],
            capture_output=True,
            check=True
        )
        return True
    except Exception as e:
        print(f"PowerShell shortcut creation failed: {e}")
        return False


def create_shortcut_with_vbs(project_root, shortcut_name, target_script, description):
    """Create shortcut using VBS script"""
    shortcut_path = os.path.expanduser(f"~\\Desktop\\{shortcut_name}.lnk")
    installer_dir = os.path.join(project_root, 'installer')

    vbs_script = f"""Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "{shortcut_path}"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = "{target_script}"
oLink.WorkingDirectory = "{project_root}"
oLink.Description = "{description}"
oLink.IconLocation = "C:\\\\Windows\\\\System32\\\\cmd.exe"
oLink.Save
"""

    vbs_path = os.path.join(installer_dir, f"create_{shortcut_name.replace(' ', '_')}.vbs")
    try:
        with open(vbs_path, 'w') as f:
            f.write(vbs_script)

        subprocess.run(
            ["cscript.exe", vbs_path],
            capture_output=True,
            check=True
        )
        os.remove(vbs_path)
        return True
    except Exception as e:
        print(f"VBS shortcut creation failed: {e}")
        if os.path.exists(vbs_path):
            os.remove(vbs_path)
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_shortcuts.py <project_root>")
        sys.exit(1)

    project_root = sys.argv[1]
    installer_dir = os.path.join(project_root, 'installer')

    if not os.path.exists(project_root):
        print(f"ERROR: Project root not found: {project_root}")
        sys.exit(1)

    print("[*] Creating desktop shortcuts...")

    # Paths
    run_server_script = os.path.join(installer_dir, 'run_server.bat')

    desktop_path = os.path.expanduser("~\\Desktop")

    success_count = 0

    # Try PowerShell first
    print("  Attempting to create shortcuts...")

    if create_shortcut_with_powershell(
        project_root,
        "Inventory Manager Server",
        run_server_script,
        "Start Inventory Management Django Server"
    ):
        print("[+] Inventory Manager Server shortcut created")
        success_count += 1
    elif create_shortcut_with_vbs(
        project_root,
        "Inventory Manager Server",
        run_server_script,
        "Start Inventory Management Django Server"
    ):
        print("[+] Inventory Manager Server shortcut created")
        success_count += 1

    if success_count == 1:
        print()
        print("[+] SUCCESS: Shortcut created on Desktop!")
        return 0
    else:
        print()
        print("[!] ERROR: Could not create shortcut automatically")
        print()
        print("[*] Manual shortcut creation:")
        print("    1. Right-click Desktop → New → Shortcut")
        print(f"    2. Target: {run_server_script}")
        print(f"    3. Name: Inventory Manager Server")
        return 1


if __name__ == "__main__":
    sys.exit(main())
