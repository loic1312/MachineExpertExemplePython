from source.BoolFact import BoolFact
from source.IntFact import IntFact
import string


class BaseFact:
    def __init__(self):
        self._listFact = []

    def pushfact(self, fact):
        if type(fact) == BoolFact or type(fact) == IntFact:
            duplicate = False
            for f in self._listFact:
                if f.getname() == fact.getname():
                    duplicate = True
            if not duplicate:
                self._listFact.append(fact)
            return True
        else:
            return False

    def getlistfact(self):
        return self._listFact

    def clearfact(self):
        self._listFact.clear()

    def searchfact(self, name=string):
        for fact in self._listFact:
            if fact.getname() == name:
                return fact

    def getvaluefact(self, name=string):
        for fact in self._listFact:
            if fact.getname() == name:
                return fact.getvalue()
