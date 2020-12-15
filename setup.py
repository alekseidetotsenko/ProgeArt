from cx_Freeze import setup, Executable

executables = [Executable('programm.py')]

setup(name='exe_art', version='0.1', description= 'progeArtProjekt', executables= executables)