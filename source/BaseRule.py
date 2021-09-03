from source.Rule import Rule
import string


class BaseRule:
    def __init__(self):
        self._listrule = []

    def clearbase(self):
        self._listrule.clear()

    def getlistrule(self):
        return self._listrule

    def setlistrule(self, list=[]):
        self._listrule = list

    def addrule(self, rule=Rule):
        self._listrule.append(rule)

    def removerule(self, namerule=string):
        for r in self._listrule:
            if r.getname() == namerule:
                self._listrule.remove(r)

    def diplaylistrule(self):
        displayrule = "Liste regle: "
        for r in self._listrule:
            displayrule = displayrule + r.getname() + ": " + r.tostring()
            displayrule = displayrule + "; "
        return displayrule
