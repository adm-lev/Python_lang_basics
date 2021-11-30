import os
import shutil


archive = 'archive'
if not os.path.exists(archive):
    os.mkdir(archive)

folder = 'my_project'
all_files = []


for root, directory, files in os.walk(folder):
    for file in files:
        if file.endswith('html'):
            all_files.append(os.path.join(root, file))

for path in all_files:
    folder_new = os.path.join(archive, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)

