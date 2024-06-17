import sys

import ollama

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
    summary = summarize_file(file_path)
    print("Summary:", summary)
