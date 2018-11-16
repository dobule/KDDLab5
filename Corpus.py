# Name: Ryan Gelston
# Class: CSC 466-01 (Fall 2018)
# Description: Stores and creates a collection of documents
import os
from Document import *


class Corpus:
    def __init__(self, docs_path, stop_word_path=None, should_stem=False):
        """ Creates an instance of a corpus

              docs_path      -- Path to documents folder
              stop_word_path -- Path to stop word file
              stem_f         -- Stemming function for corpus
        """

        # init hyper params
        self.should_stem = should_stem
        self.stop_words = []
        self.init_stop_words(stop_word_path)

        # init documents
        self.documents = []
        self.init_docs(docs_path)

        # Create the vector schema
        self.vect_schema = []

    def init_stop_words(self, stop_word_path):
        """ initializes stop words """
        if not stop_word_path:
            return

        for docname in os.listdir(os.path.abspath(stop_word_path)):
            with open(os.path.join(os.path.abspath(stop_word_path), docname),
                      'r') as f:
                self.stop_words.extend(
                    [word.strip() for word in f.readlines() if word != '\n'])

    def init_docs(self, rootdir):
        """ initializes the documents in the corpus """
        for dir in os.listdir(rootdir):
            subdir = os.path.join(os.path.abspath(rootdir), dir)
            for author_dir in os.listdir(subdir):
                docs_dir = os.path.join(subdir, author_dir)
                for docname in os.listdir(docs_dir):
                    with open(os.path.join(os.path.abspath(rootdir), dir,
                                           author_dir, docname), 'r') as f:
                        text = f.read()
                    self.documents.append(
                        Document(text, author_dir, docname, self.stop_words,
                                 self.should_stem))

    def n_docs(self):
        """ returns the number of documents """
        return len(self.documents)

    def avg_length(self):
        """ returns the average length of documents """
        return sum([len(doc.text) for doc in self.documents]) / len(
            self.documents)

    def ground_truth(self):
        """ list of (title, author) tuples for all documents """
        return [(doc.title, doc.author) for doc in self.documents]
