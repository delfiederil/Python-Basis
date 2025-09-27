import os
import shutil

# Organize files in current directory by extension
folder_map = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".txt", ".pdf", ".docx"],
    "Python": [".py"]
}

for file in os.listdir():
    for folder, extensions in folder_map.items():
        if any(file.endswith(ext) for ext in extensions):
            if not os.path.exists(folder):
                os.makedirs(folder)
            shutil.move(file, os.path.join(folder, file))
