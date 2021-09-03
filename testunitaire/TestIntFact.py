import unittest
import random
import string
from source.IntFact import IntFact

class TestIntFact(unittest.TestCase):
    def setUp(self) -> None:
        listrand = string.ascii_letters
        self.name = ''.join(random.choice(listrand) for i in range(random.randint(0, 100)))
        self.value1 = random.randint(0, 100)
        self.level1 = random.randint(0, 100)
        self.level2 = random.randint(0, 100)
        self.issue = ''.join(random.choice(listrand) for i in range(random.randint(0, 100)))
        self.intfact = IntFact(self.name, self.value1, self.level1, self.issue)

    def test_tostring(self):
        answer = self.name + "=" + str(self.value1) + "/" + str(self.level1)
        self.assertEqual(self.intfact.tostring(), answer)

    def test_level(self):
        self.assertEqual(self.intfact.getlevel(), self.level1)
        self.intfact.setlevel(self.level2)
        self.assertEqual(self.intfact.getlevel(), self.level2)

    def test_getname(self):
        self.assertEqual(self.intfact.getname(), self.name)

    def test_getissue(self):
        self.assertEqual(self.intfact.getissue(), self.issue)

    def test_getvalue(self):
        self.assertEqual(self.intfact.getvalue(), self.value1)

    def tearDown(self) -> None:
        del self.intfact
