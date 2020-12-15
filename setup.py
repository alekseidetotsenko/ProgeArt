#https://cx-freeze.readthedocs.io/en/latest/distutils.html
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", 'PIL']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name='progeArtProjekt', description= 'kunsti programm', options = {"build_exe": build_exe_options}, executables= [Executable('programm.py', base=base)])