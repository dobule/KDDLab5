# Name: Ryan Gelston and John Torres 
# Class: CSC 466-01 (Fall 2018)
# Description: Stores all of the information pertaining to a document

class Document:

    def __init__(self, text, author, title, stop_words=None, stem_f=None):
        """ Creates a document object.

              text        -- The text of the document as one string
              author      -- The author of the document
              title       -- The title of the document
              vect_schema -- List of words that represent the format of the 
                long-form word vector
              stop_words  -- List of stop words
              n_docs      -- Number of documents in the corpus
              df_vect     -- Frequency
        """

        self.length = len(text)
        self.author = author
        self.title = title
        self.text = cleanText(text, stop_words)
        self.vector = None


    @static
    def cleanText(text, stop_words, stem_f):
        """ Splits text into word tokens, removes stop words and stubs
              the remaining words.

              text -- The text of the document as one string
              stop_words -- List of stop words
        """

        # Split words

        if stop_words != None:
            # Remove stopwords

        if stem_f != None:
            # Stem remaining words

    def createFreqVect(self, vect_schema):
        """ Creates a frequency vector using the format in vect_schema
            
              text        -- List of stubbed words with stop words removed
              vect_schema -- List of words that represent the format of the 
                long-form word vector
        """
  
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
