from cx_Freeze import setup, Executable
import sys

# Include files to be bundled with the executable
includefiles = ['icon.ico']

# Dependencies
excludes = []  # List any modules to exclude from the build (if necessary)
packages = []  # List any additional packages to include (if necessary)

# Define base for Windows GUI application
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Define the MSI shortcut table
shortcut_table = [
    (
        "DesktopShortcut",            # Shortcut name
        "DesktopFolder",              # Directory where shortcut will be created
        "Billing System",             # Display name of the shortcut
        "TARGETDIR",                  # Target directory
        "[TARGETDIR]main.exe",        # Path to the executable
        None,                         # Arguments for the shortcut
        None,                         # Description
        None,                         # Hotkey
        None,                         # Icon (default)
        None,                         # Icon index
        None,                         # ShowCmd (normal window)
        "TARGETDIR",                  # Working directory
    )
]

# MSI data with shortcuts
msi_data = {"Shortcut": shortcut_table}

# MSI options
bdist_msi_options = {'data': msi_data}

# Setup configuration
setup(
    name="Billing System",
    version="0.1",
    description="A simple Billing System application",
    author="Faizan Khan",
    options={
        'build_exe': {'include_files': includefiles},
        'bdist_msi': bdist_msi_options,
    },
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
