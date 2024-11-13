import os
import shutil
import mimetypes
from pathlib import Path

def organize_files(directory):
    
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
        'Documents': ['.pdf', '.txt', '.docx', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac'],
        'Archives': ['.zip', '.tar', '.rar', '.gz'],
    }

    
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    
    for filename in os.listdir(directory):     
        file_path = os.path.join(directory, filename)   

        
        if os.path.isdir(file_path): 
            continue

        # Get file extension
        _, ext = os.path.splitext(filename) 
        ext = ext.lower() 

        
        moved = False
        for category, extensions in file_types.items():
            if ext in extensions:    
                
                category_dir = os.path.join(directory, category)  
                Path(category_dir).mkdir(parents=True, exist_ok=True) 

                
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"Moved {filename} to {category}")
                moved = True
                break

        
        if moved == False:  
            others_dir = os.path.join(directory, 'Others')
            Path(others_dir).mkdir(parents=True, exist_ok=True)
            shutil.move(file_path, os.path.join(others_dir, filename))
            print(f"Moved {filename} to Others")


folder_to_organize = 'example/path/somewhere'  #targer folder here 

organize_files(folder_to_organize)
print('Done')
