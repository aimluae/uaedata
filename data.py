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
print(res)


