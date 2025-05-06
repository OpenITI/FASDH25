import os
import stanza

# Load Stanza English pipeline
stanza.download("en")
nlp = stanza.Pipeline("en")

def clean_place_name(place_name):
    # Remove possessives like "Gaza’s"
    if place_name.endswith("'s") or place_name.endswith("’s"):
        place_name = place_name[:-2]
    return place_name.strip().lower()  # lowercase for consistency

# Step 1: Initialize dictionary
places = {}

# Step 2: Set folder path and filter January 2024 articles
folder = "/content/FASDH25-portfolio2/articles"
jan_files = [f for f in os.listdir(folder) if "2024-01" in f][:5]  # limit for testing

# Step 3: Loop through January files and extract places
for filename in jan_files:
    print("Processing:", filename)
    path = os.path.join(folder, filename)
    with open(path, encoding="utf-8") as file:
        text = file.read()
        doc = nlp(text)
        for e in doc.entities:
            if e.type in ["GPE", "LOC"]:
                place = clean_place_name(e.text)
                places[place] = places.get(place, 0) + 1

# Step 4: Export to TSV
with open("ner_counts.tsv", "w", encoding="utf-8") as out_file:
    out_file.write("placename\tcount\n")
    for place, count in sorted(places.items(), key=lambda x: -x[1]):
        out_file.write(f"{place}\t{count}\n")

# Step 5: Preview output
print("Top 10 places:")
for place, count in list(places.items())[:10]:
    print(f"{place}: {count}")
