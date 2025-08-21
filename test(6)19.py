import os
import zipfile

def compress_floder(folder_path, zip_file_name):
    zip_file = zipfile.ZipFile(zip_file_name, "w")
    
    for foldername, subfolder, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zip_file.write(file_path,os.path.relpath(file_path, folder_path))
             
    zip_file.close()
    
folder_path = "D:/Projects/PythonTests/TEST005"
zip_file_name = "compressed_folder.zip"
compress_floder(folder_path, zip_file_name)