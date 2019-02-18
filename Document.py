# Name: Ryan Gelston and John Torres 
# Class: CSC 466-01 (Fall 2018)
# Description: Stores all of the information pertaining to a document
import string
from porter import PorterStemmer
from Vector import *


class Document:
    def __init__(self, text, author, title, stop_words=None, should_stem=False):
        """ Creates a document object.

              text        -- The text of the document as one string
              author      -- The author of the document
              title       -- The title of the document
              stop_words  -- List of stop words
              freq_vector -- Word frequency vector for
        """

        self.stop_words = stop_words
        self.should_stem = should_stem
        self.porter = PorterStemmer()

        self.length = len(text)

        self.author = author
        self.title = title

        self.words = []
        self.init_words(text)
   

    def toVector(self, vect_schema, num_docs, df_vect):
        """ Creates a Vector object from the document """        
        return Vector(
                self.author,
                self.title,
                self.createFreqVect(vect_schema), 
                self.length,
                num_docs,
                df_vect)


    def init_freq_vector(self):
        """ initializes the frequency vector.
            format: v = [ (word0, count0), (word1, count1), ... ]
        """
        count = {}
        for word in self.words:
            if word in list(count.keys()):
                count[word] += 1
            else:
                count[word] = 0

        self.freq_vector = [(k, v) for k, v in count.items()]


    def init_words(self):
        """ Splits text into word tokens, removes stop words and stubs
              the remaining words.
        """
        document = self.orig_text
        for c in string.punctuation:
            document = document.replace(c, ' ')
        for word in document.split():
            word = word.strip().lower()
            should_add = True
            for c in word:
                if c not in string.ascii_letters:
                    should_add = False
            if word == '':
                should_add = False
            if not self.stop_words:
                if word in self.stop_words:
                    should_add = False
            if self.should_stem and should_add:
                word = self.porter.stem(word, 0, len(word) - 1)
            if should_add:
                self.words.append(word)

    def createFreqVect(self, vect_schema):
        """ Creates a frequency vector using the format in vect_schema
            
              word_list   -- List of stubbed words with stop words removed
              vect_schema -- List of words that represent the format of the 
                long-form word vector
        """

        freq_vect = [0] * len(vect_schema)

        for word, freq in self.df_freq:
            freq_vect[vect_schema.index(word)] = freq 

        return frew_vect
              

    def createSparseVector(self, vect_schema, n_docs, df_vect):
        """ Initializes a Vector obect in self.vector 
              
              vect_schema -- List of words that represent the format of the 
                long-form word vector
              n_docs      -- Number of documents in the corpus
              df_vect     -- Number of documents each word in vect_schema
                              appears in
        """

        

    def cosine(self, oth_doc):
        """ Finds the cosine similarity between two documents """
        if self.vector is None or oth_doc.vector is None:
            return None
        
        return self.vector.cosine(oth_doc.vector)
       
    def okapi(self, oth_doc, n_docs, df_vect, avdl, k_1, b, k_2):
        if self.vector is None or oth_doc.vector is None:
            return None

        return self.vector.okapi(oth_doc.vector, n_docs, df_vect, 
                                                 avdl, k_1, b, k_2)
