from cx_Freeze import setup, Executable
import sys

buildOptions = {'packages': [], 'excludes': []}
if sys.platform == 'win32':
    base = 'Win32GUI'
else:
    base = None

executables = [
    Executable('./src/Game.py', base=base)
]

setup(name='Raycasting Maze Game',
      version='1',
      options={'build_exe': buildOptions},
      executables=executables)