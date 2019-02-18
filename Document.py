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
        """
        self.porter = PorterStemmer()

        self.length = len(text)

        self.author = author
        self.title = title

        self.words = self.init_words(text, stop_words, should_stem)
        self.freq_vect = self.init_freq_vector()


    def toVector(self, vect_schema, num_docs, df_vect):
        """ Creates a Vector object from the document """        
        return Vector(self.createFreqVect(vect_schema), 
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

        return [(k, v) for k, v in count.items()]

    def init_words(self, orig_text, stop_words, should_stem):
        """ Splits text into word tokens, removes stop words and stubs
              the remaining words.
        """

        words = []
        document = orig_text
        for c in string.punctuation:
            document = document.replace(c, ' ')

        for word in document.split():
            word = word.strip().lower()
            should_add = True

            if word == '':
                should_add = False
            if stop_words is not None and word in stop_words:
                should_add = False

            if should_stem and should_add:
                word = self.porter.stem(word, 0, len(word) - 1)
            
            if should_add:
                words.append(word)
        return words

    def createFreqVect(self, vect_schema):
        """ Creates a frequency vector using the format in vect_schema
            
              word_list   -- List of stubbed words with stop words removed
              vect_schema -- List of words that represent the format of the 
                long-form word vector
        """
        count_vect = [0] * len(vect_schema)

        for word, freq in self.freq_vect:
            count_vect[vect_schema.index(word)] = freq 

        return [count / self.length for count in count_vect]

