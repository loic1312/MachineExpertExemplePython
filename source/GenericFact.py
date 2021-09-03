import string


class GenericFact:
    def __init__(self, name=string, level=int, issue=string):
        self._name = name
        self._level = level
        self._issue = issue
        self._value = None

    def setlevel(self, level=int):
        self._level = level

    def getname(self):
        return self._name

    def getlevel(self):
        return self._level

    def getissue(self):
        return self._issue

    def getvalue(self):
        return self._value
