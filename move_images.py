import os
import random
import shutil
import tarfile

def extract_tar(tar_path, extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with tarfile.open(tar_path, 'r') as tar:
        tar.extractall(path=extract_to)
    print(f"Extracted {tar_path} to {extract_to}")

def collect_images_in_subfolders(folder):
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
    images_by_folder = {}
    for root, _, files in os.walk(folder):
        image_files = [
            os.path.join(root, file)
            for file in files
            if os.path.splitext(file)[1].lower() in image_extensions
        ]
        if image_files:
            images_by_folder[root] = image_files
    return images_by_folder

def move_random_images_from_folders(images_by_folder, destination_folder, num_images=10):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for folder, image_paths in images_by_folder.items():
        random_files = random.sample(image_paths, min(num_images, len(image_paths)))

        folder_name = os.path.basename(folder)
        destination_subfolder = os.path.join(destination_folder, folder_name)
        if not os.path.exists(destination_subfolder):
            os.makedirs(destination_subfolder)

        for source_path in random_files:
            file_name = os.path.basename(source_path)
            destination_path = os.path.join(destination_subfolder, file_name)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name} from {folder} to {destination_subfolder}")

tar_path = "C:/652110109/Year3/coffee.tar"
extracted_folder = "C:/652110109/Year3/coffee_extracted"
destination_folder = "C:/652110109/Year3/coffee_test"

extract_tar(tar_path, extracted_folder)

images_by_folder = collect_images_in_subfolders(extracted_folder)

move_random_images_from_folders(images_by_folder, destination_folder, num_images=10)