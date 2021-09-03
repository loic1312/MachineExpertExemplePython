import string


class Rule:
    def __init__(self):
        self._name = ""
        self._listfact = []
        self._conclusion = None

    def setname(self, name=string):
        self._name = name

    def getname(self):
        return self._name

    def setconclusion(self, fact):
        self._conclusion = fact

    def getconclusion(self):
        return self._conclusion

    def setlistfact(self, list):
        self._listfact = list

    def getlistfact(self):
        return self._listfact

    def tostring(self):
        rule = "IF ("
        for r in self._listfact:
            rule = rule + r.tostring()
            rule = rule + ", "
        rule = rule + ") THEN "
        rule = rule + self._conclusion.tostring()
        return rule
