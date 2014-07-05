"""
Test python features @http://stackoverflow.com/questions/101268/hidden-features-of-python

How to run.
-----------------------------

$ python -m unittest features

"""
import unittest
class FeatureTest(unittest.TestCase) :

    def testDictComprehension(self) :
        """ Create dict with for expression """
        mdict = { i: i**2 for i in range(5) }
        target = { 0:0, 1:1, 2:4, 3:9, 4:16 }
        self.assertEqual(mdict, target)

    def testNamedFormat(self) :
        message = "The %(foo)s is %(bar)i" % { "foo": "answer", "bar": 42 }
        self.assertEqual(message, "The answer is 42")

        foo, bar = "question", 123
        message = "The %(foo)s is %(bar)i" % locals()
        self.assertEqual(message , "The question is 123")

        message = "The {foo} is {bar}".format(foo= "answer", bar=42)
        self.assertEqual(message, "The answer is 42")

    def testDictionaryGet(self) :
        """ If you do mdict.get('key')
        and key isn't there, you got back None not an excption.
        """
        mdict = { "x": 100, "y": 200 }
        self.assertEqual(mdict.get("x"), 100)
        self.assertEqual(mdict.get("y"), 200)
        self.assertEqual(mdict.get("z"), None)

    def testCreateDynamicType(self) :
        """ Createing new types in fully dynamic manner """
        MyType = type("MyType", (object,), { "x": 100, "y": 200 })
        mt = MyType()
        self.assertEqual(mt.x, 100)
        self.assertEqual(mt.y, 200)

    def testChainingComparison(self) :
        """  Chaining comparision operator """
        self.assertTrue( 1 < 2 < 3)
        self.assertTrue( 10 > 5 < 6)

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
