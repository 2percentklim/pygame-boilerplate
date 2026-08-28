#define MyAppName "Pygame Boilerplate"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Pygame Boilerplate"
#define MyAppExeName "Pygame Boilerplate.exe"

[Setup]
AppId={{8D7C2157-5FBC-4E2C-B5E4-43C53677023E}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={localappdata}\Programs\{#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=..\..\artifacts\installer
OutputBaseFilename=Pygame-Boilerplate-Setup
SetupIconFile=..\..\assets\Boilerplate-Icon.ico
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "..\..\artifacts\dist\Pygame Boilerplate\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent