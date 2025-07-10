# 📂 Downloads Organizer (Python Automation Script)

A smart Python script to automatically organize your messy **Downloads folder** (or any folder) by categorizing files into subfolders like **Images**, **Videos**, **Documents**, **Executables**, **Code**, and more.

---

## 🧠 Overview

This script helps keep your Downloads directory clean and organized by:
- Identifying file types based on extensions
- Creating categorized folders (if they don’t already exist)
- Moving files into their respective folders
- Skipping directories, `.py` script files, and `.app` bundles intelligently

---

## 🚀 Features

✅ **Automated Categorization**  
Sorts files into categories like:
- `Images`, `Videos`, `Audio`, `Documents`, `Code`, `Executables`, `Archives`, etc.

✅ **Customizable**  
You can easily edit the `file_types` dictionary to add/remove file extensions or categories.

✅ **Safe File Handling**  
Skips folders, handles exceptions gracefully, and avoids moving the script itself.

✅ **Clean Logging**  
Displays what’s being moved and where.

---

## 📂 How It Works

1. **Define Categories**  
   A dictionary (`file_types`) maps common file extensions to categories.

2. **Scan the Target Folder**  
   The script lists all items inside the specified directory.

3. **Identify File Type**  
   Based on the file extension, it assigns each file to a category. Unknown types go into the `Other` folder.

4. **Create Subfolders**  
   If a category folder doesn’t exist, it will be created automatically.

5. **Move Files**  
   The file is moved from the main folder to its new categorized location.

---

## 🛠️ Getting Started

### ✅ Prerequisites

- Python 3.x installed

### 📥 Installation

Clone this repository:
```bash
git clone https://github.com/techsavvymind-netizen/organize-downloads-with-python.git
cd organize-downloads-with-python 





