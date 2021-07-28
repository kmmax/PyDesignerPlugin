import sys
from cx_Freeze import setup, Executable

product_name = "ByteAsBits"

# base = 'Win32GUI' if sys.platform == 'win32' else None  # Избавляемся от фонового консольного окна
base = 'Win32GUI'

executables = [
    Executable(
        "bytesasbits.py",
        icon="icon.ico",
        base=base,
        target_name="ByteAsBits.exe",
        shortcut_name='ByteAsBits Application',
        shortcut_dir='ProgramMenuFolder',
    )
]

include_files = ["green_led.png", "red_led.png"]
build_exe_options = {
    "excludes": ["tkinter", "PyQt5"],
    "optimize": 2,
    'include_msvcr': True,
    "include_files": include_files

}
bdist_msi_options = {
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s' % (product_name),
    }


options = {
    'bdist_msi': bdist_msi_options,
    'build_exe': build_exe_options
}

setup(name="ByteAsBits",
      version="0.0.1",
      description="Example of custom PySide6 plugin for designer",
      executables=executables,
      options=options,
      author="Maxim Kozyakov",
      license="MIT"
)
