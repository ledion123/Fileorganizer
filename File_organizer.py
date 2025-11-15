import os
import shutil

# path must end with a slash
path = "C:/#/#/#/" 

file_names = os.listdir(path)

# Map file-types to folder names
folder_map = {
    ".csv": "csv files",
    ".pdf": "pdf files",
    ".txt": "txt files"
}

# Create folders if they don't exist
for folder in folder_map.values():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files based on extension
for file in file_names:
    file_path = os.path.join(path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    for ext, folder in folder_map.items():
        if file.endswith(ext):
            dest_path = os.path.join(path, folder, file)
            shutil.move(file_path, dest_path)
            print(f"Moved: {file} → {folder}")
