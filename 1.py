import os


#  Словарь с шаблоном
sample = {'my_project':
               ['settings', 'mainapp', 'adminapp', 'authapp']}
#  Проверка существоввния корневой папки и создание дерева.
for root, folders in sample.items():
    if os.path.exists(root):
        print(f'Папка {root} уже существует')
    else:
        for folder in folders:
            current_dir = os.path.join(root, folder)
            os.makedirs(current_dir)


