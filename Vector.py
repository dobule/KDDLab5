# Name: Ryan Gelston and John Torres
# Class: CSC 466-01 (Fall 2018)
# Description: Stores a vector in sparse vector form

import math

class Vector:

    def __init__(self, author, title, f_vect, d_len, n_docs=None, df_vect=None):
        """ Creates a sparse vector that is normalized with tfidf
              
              author  -- Author of the document the vector represents
              title   -- Title of the document the vector represents
              f_vect  -- Frequency vector in non-sparse format
              d_len   -- Length of the document in number of characters
              n_docs  -- Number of documents in corpus
              df_vect -- Number of documents each word appears in
        """
        self.author = author
        self.title = title
        self.d_len = d_len

        # If n_docs or df_vect is None, set the w_vect to f_vect
        if n_docs is None or df_vect is None:
            self.s_vect = f_vect
            return


        max_val = max(f_vect)
        s_vect = []

        tf_f = lambda t: float(t) / max_val
        idf_f = lambda df: math.log(float(n_docs) / df, 2)

        for idx, val in enumerate(f_vect):
            if val > 0:
                s_vect.append((idx, val))

        self.s_vect = [(i, tf_f(t) * idf_f(df_vect[i])) for (i, t) in s_vect]


    def ground_truth(self):
        return (self.author, self.title)


    def cosine(self, oth_vect):
        """ Computes cosine similarity between self and oth_vect """

        dot = self.dotProd(oth_vect)
        magProd = self.magnitude() * oth_vect.magnitude()

        return dot / magProd


    def dotProd(self, oth_vect):
        """ Computes dot product between this vector and another vector """
        if not len(self.s_vect) == len(oth_vect.s_vect):
            raise Exception

         totalSum = 0
         sIdx = 0
         oIdx = 0

        while sIdx < len(self.s_vect) and oIdx < len(oth_vect.s_vect):
            sItem = self.s_vect[sIdx]
            oItem = oth_vect.s_vect[oIdx]

            if sItem[0] > oItem[0]:
               oIdx += 1
            elif sItem[0] < oItem[0]:
               sIdx += 1
            else:
               totalSum += sItem[1] * oItem[1]:
               sIdx += 1
               oIdx += 1

        return totalSum


    def magnitude(self):
        """ Computes the magnitude of the vector """
        return math.sqrt(self.dotProd(self))


    def okapi(self, oth_vect, numDocs, df_vect, avgDocLen, k1, k2, b):
        """ Computes okapi distancce of two sparse vectors
              
              oth_vect  -- The other vector to find distance from
              numDocs   -- Number of documents in corpus
              df_vect   -- The number of docs each word shows up in
              avgDocLen -- Average length (in num char) for a document
              k1        -- Normalization parameter for self (usual 1.0-2.0)
              k2        -- Normalization parameter for oth_vect (usual 1-1000)
              b         -- Normalization parameter for document length (usual 0.75)
        """
        sIdx = 0
        jIdx = 0
        totalSum = 0

        df_i = len(self.s_vect)
        df_j = len(oth_vect.s_vect)

        while sIdx < len(self.s_vect) and jIdx < len(oth_vect.s_vect):

            sItem = self.s_vect[sIdx]
            oItem = oth_vect.s_vect[sIdx]

            if sItem[0] < oItem[0]:
                sIdx += 1
            elif sItem[i][0] > sItem[j][0]:
                sIdx += 1
            else:
                sVal = self.s_vect[i][1]
                oVal = oth_vect.s_vect[j][1]

                term1 = math.log((numDocs - df_vect[sIdx] + 0.5)
                                 / (d_vect[sIdx] + 0.5))
                term2 = ((k1 + sVal) 
                         / (k1 * (1 - b + b * (self.d_len / avdl)) + sVal))
                term3 = (((k2 + 1) * oVal) 
                         / (k2 + oVal))
                result += term1 * term2 * term3

       
   



