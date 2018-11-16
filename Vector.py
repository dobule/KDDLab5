# Name: Ryan Gelston and John Torres
# Class: CSC 466-01 (Fall 2018)
# Description: Stores a vector in sparse vector form

import math

class Vector:

    def __init__(self, f_vect, n_docs, df_vect):
        """ Creates a sparse vector that is normalized with tfidf """

        self.s_vect = []
        self.d_len = d_len

        max_val = max(f_vect)

        tf_f = lambda t: float(t) / max_val
        idf_f = lambda df: math.log(float(n_docs) / df, 2)

        for idx, val in enumerate(f_vect):
            if not(val is 0):
                self.s_vect.append((idx, val))


        self.w_vect = [(i, tf_f * idf_f(df_vect[i])) for i, t in self.s_vect]


    def cosine(self, oth_vect):
        """ Computes cosine similarity between self and oth_vect """

        dot = self.dotProd(oth_vect)
        magProd = self.magnitude() * oth_vect.magnitude()

        return dot / magProd


    def dotProd(self, oth_vect):
        """ Computes dot product between this vector and another vector """

        i = 0
        j = 0
        result = 0

        while i < len(self.s_vect) and j < len(oth_vect):
            if self.s_vect[i][0] < oth_vect.s_vect[j][0]:
                i = i + 1
            elif self.s_vect[i][0] > oth_vect.s_vect[j][0]:
                j = j + 1
            else:
                result = result + self.s_vect[i][1] * oth_vect.s_vect[j][1]

        return result


    def magnitude(self):
        """ Computes the magnitude of the vector """
        return math.sqrt(sum([val**2 for idx,val in self.s_vect]))


    def okapi(self, oth_vect, n_docs, df_vect, avdl, k_1, b, k_2):
        """ Computes okapi distancce of two sparse vectors
              
              oth_vect -- The other vector to find distance from
              n_docs   -- Number of documents in corpus
              df_vect  -- The number of docs each word shows up in
              avdl     -- Average length (in num char) for a document
        """

        i = 0
        j = 0
        result = 0

        df_i = len(self.s_vect)
        df_j = len(oth_vect.s_vect)

        while i < len(self.s_vect) and j < len(oth_vect):
            if self.s_vect[i][0] < self.s_vect[j][0]:
                i = i + 1
            elif self.s_vect[i][0] > self.s_vect[j][0]:
                j = j + 1
            else:
                # If same term is in both docs
                f_i = self.s_vect[i][1]
                f_j = oth_vect.s_vect[j][1]
                term1 = math.log((n_docs - df_vect[i] + 0.5) /
                                 (d_vect[i] + 0.5))
                term2 = ((k_1 + f_i) / 
                         (k_1 * (1 - b + b * (self.d_len / avdl)) + f_i))
                term3 = (((k_2 + 1) * f_j) /
                         (k_2 + f_j))
                result = result + math.log(term1 * term2 * term3)

       




