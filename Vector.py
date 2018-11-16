# Name: Ryan Gelston and John Torres
# Class: CSC 466-01 (Fall 2018)
# Description: Stores a vector in sparse vector form

import math

class Vector:

    def __init__(self, f_vect):

        self.s_vect = []


        for idx, val in enumerate(f_vect):
            if not(val is 0):
                self.s_vect.append((idx, val))

        n = len(self.s_vect)

        idf_f = 

        for i in range(len(self.s_vect)):
            self.s_vect[i][1] = (self.s_vect[i][0], self.s_vect


         
    def cosine(self, oth_vect):
        """ Computes cosine similarity between self and oth_vect """

        dot = self.dotProd(oth_vect)
        magProd = self.magnitude() * oth_vect.magnitude()

        return dot / magProd

    def dotProd(self, oth_vect):

        i = 0
        j = 0
        result = 0

        while i < len(self.s_vect) and j < len(oth_vect):
            if self.s_vect[i][0] < self.s_vect[j][0]:
                i = i + 1
            elif self.s_vect[i][0] > self.s_vect[j][0]:
                j = j + 1
            else:
                result = result + self.s_vect[i][1] * self.oth_vect[j][1]

        return result

    def magnitude(self):
        return math.sqrt(sum([val**2 for idx,val in self.s_vect]))
                


    def okapi(self, oth_vect):
        """ Computes """

        




