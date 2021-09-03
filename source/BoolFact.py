from source.GenericFact import GenericFact
import string


class BoolFact(GenericFact):
    def __init__(self, name=string, value=bool, level=int, issue=string):
        super(BoolFact, self).__init__(name, level, issue)
        self._value = value

    def tostring(self):
        return self._name + "=" + str(self._value) + "/" + str(self._level)