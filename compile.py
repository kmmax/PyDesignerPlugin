"""
Script is used for converting files is gotten PySide6-designer (*.ui) to *.py file.
This is additional tool.
"""

import os

os.system(
    "D:\_Development\Python\env_root\Scripts\pyside6-uic.exe ui_bytesasbits.ui \
    -o ui_bytesasbits.py"
)
