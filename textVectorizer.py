import sys
import os

ROOT_DIR = sys.argv[1]

documents = {}

for dir in os.listdir(ROOT_DIR):
    subdir = os.path.join(os.path.abspath(ROOT_DIR), dir)
    for author_dir in os.listdir(subdir):
        if author_dir not in documents:
            documents[author_dir] = {}
        docs_dir = os.path.join(subdir, author_dir)
        for docname in os.listdir(docs_dir):
            with open(os.path.join(os.path.abspath(ROOT_DIR), dir, author_dir, docname), 'r') as f:
                text = f.readlines()
            documents[author_dir][docname] = text

stop_words = []

for docname in os.listdir(os.path.abspath('./StopWords')):
    with open(os.path.join(os.path.abspath('./StopWords'), docname), 'r') as f:
        stop_words.extend([word.strip() for word in f.readlines() if word != '\n'])

for author in documents.keys():
    for document_name in documents[author]:
        document = documents[author][document_name]
        for word in stop_words:
            document = document.replace(word, '')
        documents[author][document_name] = document






