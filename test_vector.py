import unittest
import Vector
import math


def create_vector():
    f_vect = [1, 1, 2, 4]
    d_len = 35
    n_docs = 1
    df_vect = [1, 1, 1, 1]
    return Vector(f_vect, d_len, n_docs, df_vect)


def create_vector_two():
    f_vect_two = [2, 2, 2, 4]
    d_len_two = 40
    n_docs_two = 2
    df_vect_two = [2, 2, 2, 2]
    return Vector(f_vect_two, d_len_two, n_docs_two, df_vect_two)


class VectorTest(unittest.TestCase):
    def test_dot_product(self):
        v = create_vector()
        v_two = create_vector_two()
        result = v.dotProd(v_two)
        expected = 2 + 2 + 4 + 16
        self.assertEqual(result, expected, msg="dot product")

    def test_magnitude(self):
        v = create_vector()
        result = v.magnitude()
        expected = math.sqrt(sum([val**2 for idx, val in v.s_vect]))
        self.assertEqual(result, expected, msg="magnitude")

    def test_cosine(self):
        v = create_vector()
        v_two = create_vector_two()
        result = v.cosin(v_two)
        expected = (2 + 2 + 4 + 16) / (v.magnitude() * v_two.magnitude())
        self.assertEqual(result, expected, msg="cosine")

    def test_okapi(self):
        pass

