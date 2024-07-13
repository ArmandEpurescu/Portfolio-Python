import os
import shutil


path = r"C:/Users/Armand Epurescu/Downloads/"

file_name = os.listdir(path)

file_categories = {
    "csv files": [".csv"],
    "image files": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "text files": [".txt", ".doc", ".docx", ".pdf", ".rtf", ".odt"],
    "excel files": [".xls", ".xlsx"]
}


for folder in file_categories.keys():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)




for file in file_name:
    file_lower = file.lower()  
    moved = False
    for folder, extensions in file_categories.items():
        if any(file_lower.endswith(ext) for ext in extensions):
            destination = os.path.join(path, folder, file)
            if not os.path.exists(destination):
                shutil.move(os.path.join(path, file), destination)
                moved = True
            break
    if not moved:
        print(f"There are files in this path that were not moved: {file}")