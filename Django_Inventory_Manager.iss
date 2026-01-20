[Setup]
AppName=Django Inventory Manager
AppVersion=1.0.0
AppPublisher=Inventory Management System
AppCopyright=2026
DefaultDirName={autopf}\Django Inventory Manager
DefaultGroupName=Django Inventory Manager
OutputDir=dist\installer
OutputBaseFilename=Django_Inventory_Manager_Setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
AllowNoIcons=yes
SetupIconFile=
WizardStyle=modern
UninstallDisplayIcon={app}\Django_Inventory_Manager.exe
DisableStartupPrompt=no
ShowLanguageDialog=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\Django_Inventory_Manager.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Django Inventory Manager"; Filename: "{app}\Django_Inventory_Manager.exe"; WorkingDir: "{app}"
Name: "{commondesktop}\Django Inventory Manager"; Filename: "{app}\Django_Inventory_Manager.exe"; WorkingDir: "{app}"

[Run]
Filename: "{app}\Django_Inventory_Manager.exe"; Description: "Launch Django Inventory Manager"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{app}\*"
Type: dirsempty; Name: "{app}"

[Messages]
WelcomeLabel1=Welcome to the Django Inventory Manager Setup
WelcomeLabel2=This will install Django Inventory Manager on your computer.
FinishedHeadingText=Completed
FinishedLabelText=Setup has finished installing Django Inventory Manager. The application will now start.
