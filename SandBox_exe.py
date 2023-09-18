import cx_Freeze
from gat_all_files import get_files
all_files = get_files()

executables = [cx_Freeze.Executable('game.py',
                                    base='Win32GUI',
                                    icon='images/icon.ico',
                                    shortcut_dir='DesktopFolder',
                                    shortcut_name='SandBox')]
cx_Freeze.setup(
    name='SandBox', options={'build.exe': {'packages': ['pygame'],
                                           'include_files': all_files}},
    executables=executables)
