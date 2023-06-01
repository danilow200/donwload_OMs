import sys
from cx_Freeze import setup, Executable

build_exe_options = {
  'packages': ['selenium', 'PySimpleGUI'],
  'excludes': [],
  'include_files': ['omRelatorio.py', 'assets']
}

base = None

if sys.platform == "win32":
  base = "Win32GUI"

icone = './assets/icontelebras_resized.ico'

executables = [Executable('layout.py', base=base, icon= icone)]

setup(
  name='Dowload de Relatórios',
  version='0.1',
  description='Este programa baixa relatórios automaticamente na OM :) ',
  options={'build_exe': build_exe_options},
  executables=executables
)