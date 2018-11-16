import sys
import os
import re
import string
import argparse
from porter import *

parser = argparse.ArgumentParser()
parser.add_argument('rootdir', help='root directory of rutgers dataset')
parser.add_argument('-sw', '--stop-words', action='store_true', help='enable stop word removal')
parser.add_argument('-st', '--stem', action='store_true', help='enable stemming')
parser.add_argument('--ground-truth', action='store', help='ground truth output filename')
args = parser.parse_args()

ROOT_DIR = args.rootdir
REMOVE_STOP_WORDS = args.stop_words
STEMMING = args.stem
GT_OUTFILE = args.ground_truth

documents = {}

for dir in os.listdir(ROOT_DIR):
    subdir = os.path.join(os.path.abspath(ROOT_DIR), dir)
    for author_dir in os.listdir(subdir):
        if author_dir not in documents:
            documents[author_dir] = {}
        docs_dir = os.path.join(subdir, author_dir)
        for docname in os.listdir(docs_dir):
            with open(os.path.join(os.path.abspath(ROOT_DIR), dir, author_dir, docname), 'r') as f:
                text = f.read()
            documents[author_dir][docname] = text

stop_words = []

for docname in os.listdir(os.path.abspath('./StopWords')):
    with open(os.path.join(os.path.abspath('./StopWords'), docname), 'r') as f:
        stop_words.extend([word.strip() for word in f.readlines() if word != '\n'])

for author in documents.keys():
    porter = PorterStemmer()

    for document_name in documents[author].keys():
        document = documents[author][document_name]
        words = []
        for word in document.split():
            word = word.strip().strip(string.punctuation).lower()
            should_add = True
            if word == '':
                should_add = False
            if not word.isalpha:
                should_add = False
            if REMOVE_STOP_WORDS:
                if word in stop_words:
                    should_add = False
            if STEMMING and should_add:
                word = porter.stem(word, 0, len(word) - 1)
            if should_add:
                words.append(word)
        print(words)
        documents[author][document_name] = words

if GT_OUTFILE:
    ground_truth = []
    for author in documents.keys():
        for document_name in documents[author].keys():
            ground_truth.append((document_name, author))
    with open('ground_truth.txt', 'w') as f:
        conv_gt = [','.join(list(entry)) for entry in ground_truth]
        f.write('\n'.join(conv_gt))

