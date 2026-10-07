import os
import sys

def rename_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('educationswap', 'educationswap')
        new_content = new_content.replace('EducationSwap', 'EducationSwap')
        new_content = new_content.replace('EDUCATIONSWAP', 'EDUCATIONSWAP')
        new_content = new_content.replace('Educationswap', 'Educationswap')
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        print(f"Skipping {file_path} due to read/write error: {e}")

def main(root_dir):
    # First, replace contents in files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip git directory
        if '.git' in dirpath:
            continue
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Skip some binary/image files
            if not any(file_path.endswith(ext) for ext in ['.pyc', '.png', '.jpg', '.jpeg', '.mp4', '.ico', '.svg', '.bin']):
                rename_content(file_path)

    # Then rename directories and files bottom-up to avoid invalidating paths
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if '.git' in dirpath:
            continue
        
        # Rename files
        for filename in filenames:
            if 'educationswap' in filename.lower():
                new_filename = filename.replace('educationswap', 'educationswap').replace('EducationSwap', 'EducationSwap')
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)
                
        # Rename directories
        for dirname in dirnames:
            if 'educationswap' in dirname.lower():
                new_dirname = dirname.replace('educationswap', 'educationswap').replace('EducationSwap', 'EducationSwap')
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, new_dirname)
                os.rename(old_path, new_path)

if __name__ == '__main__':
    main('/Users/mohammadhasnattalukder/Downloads/Compressed/educationswap-3.9.1')
