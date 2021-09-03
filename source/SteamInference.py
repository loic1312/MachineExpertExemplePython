from source.IhmSteamExpert import IhmSteamExpert
from source.BaseRule import BaseRule
from source.BaseFact import BaseFact
from source.Rule import Rule
from source.FactFactory import FactFactory
import string

class SteamInference:
    def __init__(self, ihm=IhmSteamExpert):
        self._ihm = ihm
        self._baserule = BaseRule()
        self._basefact = BaseFact()
        self._levelmaxrule = 0

    def getint(self, issue=string):
        self._ihm.getintvalue(issue)

    def getbool(self, issue=string):
        self._ihm.getboolvalue(issue)

    def isrelevant(self, rule=Rule):
        levelmax = -1
        for f in rule.getlistfact():
            factfind = self._basefact.searchfact(f.getname())
            if factfind is None:
                if f.getissue() is not None:
                    factory = FactFactory()
                    factfind = factory.createfact(f, self._ihm)
                    self._basefact.pushfact(factfind)
                else:
                    return -1
            if f.getvalue() != factfind.getvalue():
                return -1
            else:
                levelmax = max([factfind.getlevel(), levelmax])
        return levelmax

    def findrule(self, baserulelocal=BaseRule()):
        for r in baserulelocal.getlistrule():
            level = self.isrelevant(r)
            if level is not -1:
                self._levelmaxrule = level
                return r

    def solve(self):
        baserulelocal = BaseRule()
        baserulelocal.setlistrule(self._baserule.getlistrule())
        self._basefact.clearfact()
        r = self.findrule(baserulelocal)
        while r != None:
            f = r.getconclusion()
            f.setlevel(self._levelmaxrule + 1)
            self._basefact.pushfact(f)
            baserulelocal.removerule(r.getname())
            r = self.findrule(baserulelocal)
        self._ihm.displayfact(self._basefact.getlistfact())

    def stringtorule(self, r=string):
        #une régle: nomregle:p1,p1,p3:c
        r.strip()
        listrule = str.split(r, ':')
        if len(listrule) is not 0:
            factfactory = FactFactory()
            factconclusion = factfactory.stringtofact(listrule[2])
            listpstring = str.split(listrule[1], ',')
            listp = []
            for f in listpstring:
                listp.append(factfactory.stringtofact(f))
            rule = Rule()
            rule.setconclusion(factconclusion)
            rule.setlistfact(listp)
            rule.setname(listrule[0])
            self._baserule.addrule(rule)
