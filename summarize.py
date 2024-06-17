import sys
import os

import docx2txt
import PyPDF2
import ollama

def read_file_content(file_path):
    # Überprüfen, ob die Datei existiert
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Die Datei {file_path} wurde nicht gefunden.")
    
    # Dateiendung extrahieren
    file_extension = os.path.splitext(file_path)[1].lower()
    
    # Inhalt der Datei basierend auf der Dateiendung auslesen
    if file_extension == '.docx':
        # Word-Dokument
        content = docx2txt.process(file_path)
    elif file_extension == '.pdf':
        # PDF-Dokument
        content = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                content += page.extract_text()
    elif file_extension == '.txt' or file_extension == '.md':
        # Reine Text-Datei
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    else:
        raise ValueError(f"Die Dateiendung {file_extension} wird nicht unterstützt.")
    
    return content


def summarize_content(content):
    prompt = "Deine Aufgabe ist es, den gegebenen Text in ungefähr 300 Wörtern zusammenzufassen. Gebe nur die Zusammenfassung wieder ohne weitere Angaben."
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                'role': 'user',
                'content': f"{prompt}. Das ist der Text: {content}"
            },
        ],
        )
    summary = response['message']['content']
    return summary


def summarize_file(file_path):
    # Fasse den Inhalt der übergebenen Datei zusammen
    with open(file_path, 'r') as file:
        file_content = file.read()
        prompt = "Deine Aufgabe ist es, den gegebenen Text in ungefähr 300 Wörtern zusammenzufassen. Gebe nur die Zusammenfassung wieder ohne weitere Angaben."
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    'role': 'user',
                    'content': f"{prompt}. Das ist der Text: {file_content}"
                },
            ],
        )
    summary = response['message']['content']
    return summary

# Beispielaufruf
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 summarize.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    content = read_file_content(file_path=file_path)
    summary = summarize_content(content)
    print(summary)
