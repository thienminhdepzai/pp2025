import os
import zipfile as zf

def compress_data(files_to_compress=None):
    if files_to_compress is None:
        files_to_compress = [
            "info/students.txt", 
            "info/courses.txt", 
            "info/marks.txt"
        ]
    
   
    with zf.ZipFile("students.dat", "w", zf.ZIP_DEFLATED) as zipf:
        for file in files_to_compress:
            if os.path.exists(file):
                zipf.write(file)
    print("Data compressed successfully!")
    