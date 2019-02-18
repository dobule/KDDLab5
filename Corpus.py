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

        self.num_docs = len(self.documents)

        self.all_words_schema = self.all_words()


    def listOfVectors(self, vect_schema):
        """ Returns a list of Vector objects where each Vector represents a
            particular document.
        """

        return [doc.toVector(
                  vect_schema, 
                  self.df_vect(vect_schema),
                  self.num_docs) 
                for doc in self.documents] 


    def init_stop_words(self, stop_word_path):
        """ initializes stop words """
        if stop_word_path is None:
            return None

        with open(stop_word_path, 'r') as f:
            self.stop_words.extend(
              [word.lstrip().rstrip() 
                for word in f.readlines() 
                if not word.isspace()])


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

    def df_vect(self, vector_schema):
        """ Creates a document frequency vector for the passed vector schema
        """
        
        count_vect = [0] * len(vector_schema)

        for idx, word in enumerate(vector_schema):
            for doc in self.documents:
                if word in doc.words:
                    count_vect[idx] = count_vect[idx] + 1

        return [count / self.num_docs for count in count_vect]
                    
                    

    def all_words(self):
        """ Returns a list of all words in the corpus """
        
        all_words = set()

        for doc in self.documents:
            for word in doc.words:
                all_words.add(word)

        return list(all_words)


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


