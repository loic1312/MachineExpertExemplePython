import unittest
import random
import string
from source.GenericFact import GenericFact


class TestGenericFact(unittest.TestCase):
    def setUp(self) -> None:
        listrand = string.ascii_letters
        self.name = ''.join(random.choice(listrand) for i in range(random.randint(0, 100)))
        self.level1 = random.randint(0, 100)
        self.level2 = random.randint(0, 100)
        self.issue = ''.join(random.choice(listrand) for i in range(random.randint(0, 100)))
        self.genericfact = GenericFact(self.name, self.level1, self.issue)

    def test_getname(self):
        self.assertEqual(self.genericfact.getname(), self.name)

    def test_level(self):
        self.assertEqual(self.genericfact.getlevel(), self.level1)
        self.genericfact.setlevel(self.level2)
        self.assertEqual(self.genericfact.getlevel(), self.level2)

    def test_getissue(self):
        self.assertEqual(self.genericfact.getissue(), self.issue)

    def test_getvalue(self):
        self.assertEqual(self.genericfact.getvalue(), None)

    def tearDown(self) -> None:
        del self.genericfact
