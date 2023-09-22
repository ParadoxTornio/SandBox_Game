import cx_Freeze

# from gat_all_files import get_files
# all_files = get_files()
all_files = ['background.png',
             'background_2.png',
             'bricks.png',
             'bricks_frame.png',
             'buffed_metal.png',
             'button.png',
             'button_0.png',
             'C4.png',
             'C4_frame.png',
             'concrete.png',
             'concrete_frame.png',
             'config.py',
             'elements.py',
             'esc_button.png',
             'fire.png',
             'fire_frame.png',
             'game.py',
             'gat_all_files.py',
             'glass.png',
             'glass_frame.png',
             'gunpowder.png',
             'gunpowder_frame.png',
             'lava.png',
             'lava_frame.png',
             'menu.py',
             'metal.png',
             'metal_frame.png',
             'metal_plus_frame.png',
             'musorka.png',
             'oak.png',
             'oak_frame.png',
             'PixeloidMono-d94EV.ttf',
             'poison.png',
             'poison_frame.png',
             'sand.png',
             'SandBox_exe.py',
             'sand_frame.png',
             'stone.png',
             'stone_frame.png',
             'test_frame.png',
             'utils.py',
             'water.png',
             'water_frame.png',
             'пар.png']

executables = [cx_Freeze.Executable('game.py',
                                    base='Win32GUI',
                                    icon='icon.ico',
                                    shortcut_dir='DesktopFolder',
                                    shortcut_name='SandBox')]
cx_Freeze.setup(
    name='SandBox', options={'build_exe': {'packages': ['pygame'],
                                           'include_files': all_files}},
    executables=executables)
