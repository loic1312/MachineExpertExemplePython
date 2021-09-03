import unittest
from source.FactFactory import FactFactory


class TestFactFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.fint = "test1=3=c'est un int?"
        self.fbool = "test2/true/c'est un bool?"
        self.factfactory = FactFactory()

    def test_stringfact(self):
        #a faire
