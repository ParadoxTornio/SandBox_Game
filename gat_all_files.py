import os


def get_files():
    all_files = []
    files = os.listdir()
    for file in files:
        if (file.endswith('.py') or file.endswith('.ttf')) and file != 'SandBox.py':
            all_files.append(file)
    for root, _, dir_files in os.walk('images'):
        for file in dir_files:
            all_files.append(os.path.join(root, file))
    print(all_files)
    return all_files
