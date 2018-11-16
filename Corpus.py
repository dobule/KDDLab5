# Name: Ryan Gelston
# Class: CSC 466-01 (Fall 2018)
# Description: Stores and creates a collection of documents

class Corpus:

    def __init__(self, docs_path, stop_word_path=None, stem_f=None):
        """ Creates an instance of a corpus

              docs_path      -- Path to documents folder
              stop_word_path -- Path to stop word file
              stem_f         -- Stemming function for corpus
        """

        # Go through all documents in docs_path and create Document
        #   objects for each of them
        self.documents = []

        # Find average length of the documents
        self.avdl = 0

        # Find number of documents in corpus
        self.n_docs = 0

        # Create the vector shema
        self.vect_schema = []


