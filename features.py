"""
Test python features @http://stackoverflow.com/questions/101268/hidden-features-of-python

How to run.
-----------------------------

$ python -m unittest features

"""
import unittest
class FeatureTest(unittest.TestCase) :

    def testGetAttribute(self) :
        """ The getattr build-in function """
        class C() :
            def getMonths(self) :
                return ["January", "Febuary", "March"]

        c = C()
        months = getattr(c, "getMonths")()
        self.assertEqual(months, ["January", "Febuary", "March"])

    def testMultipleLineRegex(self) :
        """ Regular expression as verbose mode """
        import re
        pattern = """
        ^       # can have comments
        M{0,4}
        u{5}
        K{0,4}
        $"""
        test = "MMuuuuuKKKK"
        match = re.search(pattern, test, re.VERBOSE)
        self.assertEqual(match.group(), test)

    def testMonkeypatchingObject(self) :
        """ Create quick dirty object wiht __dict__. """
        class C() :
            def __init__(self, **kwargs) :
                self.__dict__.update(kwargs)

        c = C(name="wk", home="kk")
        self.assertEqual(c.name, "wk")
        self.assertEqual(c.home, "kk")


    def testOperatorOverloadForSet(self) :
        """ Operator overloading for the set buildin """
        a = set([1,2,3,4])
        b = set([3,4,5,6])
        union = a | b
        intersect = a & b
        subset = a < b
        diff = a - b
        symetricDif = a ^ b
        self.assertEqual(union, {1,2,3,4,5,6})
        self.assertEqual(intersect, {3,4})
        self.assertEqual(subset, False)
        self.assertEqual(diff, {1,2})
        self.assertEqual(symetricDif, {1,2,5,6})
