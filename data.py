import os
from pathlib import Path


# folder path
dir_path = r'./datasets'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        path = Path(path).stem
        res.append(path)

res.remove('.DS_Store')
res = [item.replace(" ", "_") for item in res]

print(res)

lines = res
with open('data_name.txt', 'w') as f:
    f.writelines('\n'.join(lines))

    