import os


all_files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        all_files.append(os.stat(file_path).st_size)
max_size = max(all_files)
i = 1
out_dict = {}
for n in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0
for file in all_files:
    out_dict[10 ** len(str(file))] += 1
print(out_dict)
