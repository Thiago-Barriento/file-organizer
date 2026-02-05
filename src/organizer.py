# organizer.py
# Arquivo responsável pela lógica de organização dos arquivos

import os
import shutil
from config import FILE_CATEGORIES

def organize_files(folder_path):
    """
    Organiza os arquivos de uma pasta de acordo com suas extensões.
    """

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            organize_single_file(file_path, folder_path)

def organize_single_file(file_path, base_folder):
    file_extension = os.path.splitext(file_path)[1].lower()
    destination_folder = get_destination_folder(file_extension)

    if destination_folder:
        create_folder_if_not_exists(base_folder, destination_folder)
        move_file(file_path, base_folder, destination_folder)

def get_destination_folder(extension):
    for folder_name, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return folder_name
    return "Outros"

def create_folder_if_not_exists(base_folder, folder_name):
    folder_path = os.path.join(base_folder, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def move_file(file_path, base_folder, destination_folder):
    destination_path = os.path.join(base_folder, destination_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)
