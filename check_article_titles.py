import re
import os

articles_dir = "python_exercises/lesson_8.1/aljazeera_articles"

for article in os.listdir(articles_dir):
    article_path = os.path.join(articles_dir, article)

    with open(article_path, "r", encoding="utf8") as f:
        text = f.read()
    
    regex = r"\n+-+\n"
    title = re.split(regex, text)[0]

    no_matches = len(re.findall(r"Gazan?", title))
    if no_matches > 0:
        print(article)
        print(no_matches)
        