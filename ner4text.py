import os
import spacy

# nlp = spacy.load("de_dep_news_trf")
# nlp = spacy.load("de_core_news_sm")
nlp = spacy.load("de_core_news_lg")

directory = "../bot/bot/bot/data_altenhein/"

all_entities = []

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(os.path.join(directory, filename), "r", encoding="utf-8") as file:
            text = file.read()
            doc = nlp(text)

            entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ["PER", "LOC"]]
            # print(f"Entitäten in {filename}:")
            # print(entities)
            all_entities.extend(entities)

unique_entities = list(set(all_entities))

print(unique_entities)
print(len(unique_entities))
