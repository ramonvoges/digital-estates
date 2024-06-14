import os
import pandas as pd
from datetime import datetime
import sys

def get_file_info(directory_path):
    file_info_list = []
    for root, dirs, files in os.walk(directory_path):
        for i, file in enumerate(files, start=1):
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            file_extension = os.path.splitext(file)[1]
            file_info = {
                "Laufende Nummer": i,
                "Dateiname": file,
                "Dateiendung": file_extension,
                "Dateipfad": file_path,
                "Änderungsdatum": datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                "Erstellungsdatum": datetime.fromtimestamp(file_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                "Dateigröße (Bytes)": file_stats.st_size,
                "Bemerkungen": ""
            }
            file_info_list.append(file_info)
    return file_info_list

def create_excel(file_info_list, output_file):
    df = pd.DataFrame(file_info_list)
    df.to_excel(output_file, index=False)

def main(directory_path, output_file):
    file_info_list = get_file_info(directory_path)
    create_excel(file_info_list, output_file)
    print(f"Excel-Datei '{output_file}' wurde erfolgreich erstellt.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python file_list_generator.py <directory_path> <output_file>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    output_file = sys.argv[2]
    main(directory_path, output_file)

