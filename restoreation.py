import os
import shutil

def restore_downloads(target_directory):
    for folder in os.listdir(target_directory):
        folder_path = os.path.join(target_directory, folder)
        if os.path.isdir(folder_path):
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                destination = os.path.join(target_directory, item)
                try:
                    shutil.move(item_path, destination)
                    print(f"Restored '{item}' from '{folder}'")
                except Exception as e:
                    print(f"Error restoring '{item}': {e}")

    print("Restoration Complete")

# Use the same path
my_download_path = r"D:\zalanda_project\Downloads"

if __name__ == "__main__":
    restore_downloads(my_download_path)