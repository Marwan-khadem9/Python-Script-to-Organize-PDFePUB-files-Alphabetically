import os
import shutil

def organize_files(source_folder, destination_folder):
    # Ensuring the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Getting a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # Filtering out only PDF and EPUB files
    filtered_files = [f for f in files if f.lower().endswith(('.pdf', '.epub'))]
    
    # Sorting files alphabetically
    sorted_files = sorted(filtered_files)
    
    # Moving files to the destination folder
    for file in sorted_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {destination_folder}")

if __name__ == "__main__":
    # Defining my source and destination folders here
    source_folder = "E:\Books"
    destination_folder = "E:\Organized Books"
    
    organize_files(source_folder, destination_folder)
