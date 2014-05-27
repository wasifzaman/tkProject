import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

#"packages": ["os"],
#"includes": ["tkinter", "datetime", "pickle", "PIL",
#"xlsxwriter", "xlrd", "tkinter.messagebox",
#"tkinter.filedialog", "PIL.Image", "PIL.ImageTk"],
#"include_files": ["rybDB.db", "rybCONFIG.db"],
#"icon": "ryb_color_shadow2.ico"}'''

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {}

setup(  name = "rybDB",
        version = "0.1",
        description = "RYB DB",
        options = {"build_exe": build_exe_options},
        executables = [Executable("splashy2.py", base=base)])
