from pip._vendor.distlib.compat import raw_input
from source.BaseRule import BaseRule
import string


class IhmSteamExpert:
    def getintvalue(self, issue=string):
        value = raw_input(issue)
        return int(value)

    def getboolvalue(self, issue=string):
        value = raw_input(issue)
        if value == "True":
            return True
        else:
            return False

    def displayfact(self, listfact=[]):
        listfact = sorted(listfact, key=lambda fact: fact.getlevel())
        for f in listfact:
            if f.getlevel() != -1:
                print(f.tostring())

    def displayrule(self, baserule=BaseRule):
        baserule.diplaylistrule()
