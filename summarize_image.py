import sys

import ollama

def summarize_image(file_path):
    # Fasse den Inhalt der übergebenen Bilddatei zusammen
    with open(file_path, 'r') as file:
        file_content = file.read()
        prompt = "Deine Aufgabe ist es, das gegebenen Bild in ungefähr 300 Wörtern zusammenzufassen. Gebe nur die Zusammenfassung wieder ohne weitere Angaben."
        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                    'images': [file.read()],
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
    summary = summarize_image(file_path)
    print("Summary:", summary)
