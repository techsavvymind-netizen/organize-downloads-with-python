import os
import shutil

def organize_downloads(target_directory):
    if not os.path.exists(target_directory):
        print(f"Error:the directory'{target_directory}' not exists")
        return
    print(f"Starting to organize:{target_directory}")

    file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".heic"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Executables": [".exe", ".msi", ".dmg", ".app", ".deb", ".rpm", ".run", ".sh",  ".bat", ".com",".bin",".apk",  ".jar",],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".php", ".json", ".xml", ".ipynb"],
    "Spreadsheets": [".csv", ".xlsx", ".xls"], # Specific for spreadsheets if you want
    "Presentations": [".pptx", ".ppt"], # Specific for presentations
    "Torrents": [".torrent"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Web_Files": [".html", ".htm", ".css", ".js", ".php"], # Can overlap with Code, depends on preference
    "Temporary": [".tmp", ".temp", ".~lock"], # Files that might be temporary or incomplete downloads
    "Disk_Images": [".iso", ".img", ".vhd", ".vmdk"],
    }
    
    items=os.listdir(target_directory)
    for item in items:
        item_path=os.path.join(target_directory,item)
        if os.path.isdir(item_path):
            if item.endswith(".app"):
                pass
            else:
                continue

        if item.endswith(".py"):
            continue

        file_name,file_extention=os.path.splitext(item)
        file_extention=file_extention.lower()

        found_category ="other"
        for category,extentions in file_types.items():
            if file_extention in extentions:
                found_category=category
                break

        if item.endswith(".app") and found_category=="other":
            found_category="Executables"

        destination_folder=os.path.join(target_directory , found_category)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Folder created: {found_category}")
        
        destination_path = os.path.join(destination_folder,item)


        try:
            shutil.move(item_path,destination_path)
            print(f"Moveed '{item}' to '{found_category}'")
        except shutil.Error  as e:
            print(f"error moving '{item}' :'{e}'")

        except Exception as e :
            print(f"an error occur '{item}':'{e}'")


    print("Organization Complete")


my_download_path="D:\zalanda_project\Downloads"


if __name__=="__main__":
    organize_downloads(my_download_path)
  
    










