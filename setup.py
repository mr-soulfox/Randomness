import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "matplotlib"], "includes": ["tkinter"]}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name="Randomness",
    version="1.0",
    description="Plot Randomness with numbers",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
