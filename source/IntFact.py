from source.GenericFact import GenericFact
import string


class IntFact(GenericFact):
    def __init__(self, name=string, value=int, level=int, issue=string):
        super(IntFact, self).__init__(name, level, issue)
        self._value = value

    def tostring(self):
        return self._name + "=" + str(self._value) + "/" + str(self._level)
