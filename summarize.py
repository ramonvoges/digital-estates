import requests
import sys

import ollama

def summarize_file(file_path):
    # Fasse den Inhalt der übergebenen Datei zusammen
    with open(file_path, 'r') as file:
        file_content = file.read()
        prompt = "Deine Aufgabe ist es, den gegebenen Text in ungefähr 300 Wörtern zusammenzufassen. Gebe nur die Zusammenfassung wieder ohne weitere Angaben."
        text = f"Das ist der Text: {file_content}"
        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    'role': 'user',
                    'content': f"{prompt} {text}"
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
    summary = summarize_file(file_path)
    print("Summary:", summary)
