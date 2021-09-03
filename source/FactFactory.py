#from source.SteamInference import SteamInference
from source.IntFact import IntFact
from source.BoolFact import BoolFact
from source.IhmSteamExpert import IhmSteamExpert
import string


class FactFactory:
    def createfact(self,  fact, ihm=IhmSteamExpert):
        if type(fact) == IntFact:
            value = ihm.getintvalue(fact.getissue())
            return IntFact(fact.getname(), value, 0, "")
        elif type(fact) == BoolFact:
            value = ihm.getboolvalue(fact.getissue())
            return BoolFact(fact.getname(), value, 0, "")
        else:
            return None

    def stringtofact(self, f=string):
        f.strip()
        if '=' in f:
            # c'est un fait entier: nom=valeur=question
            listfact = str.split(f, '=')
            if len(listfact) == 3:
                return IntFact(listfact[0], int(listfact[1]), 0, listfact[2])
            else:
                return IntFact(listfact[0], int(listfact[1]), 0, None)
        elif '/' in f:
            # c'est un fait booleen: nom/valeur/question
            listfact = str.split(f, '/')
            if listfact[1] == "True":
                value = True
            else:
                value = False
            if len(listfact) == 3:
                return BoolFact(listfact[0], value, 0, listfact[2])
            else:
                return BoolFact(listfact[0], value, 0, None)
        else:
            return None

