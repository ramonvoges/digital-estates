import docx2txt
import os
import sys

def convert_docx_to_txt(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".docx"):
            docx_path = os.path.join(input_folder, filename)
            txt_path = os.path.join(output_folder, filename.replace(".docx", ".txt"))
            
            text = docx2txt.process(docx_path)
            with open(txt_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python word2txt.py <input_folder> <output_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    convert_docx_to_txt(input_folder, output_folder)