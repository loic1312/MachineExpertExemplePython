from source.IhmSteamExpert import IhmSteamExpert
from source.SteamInference import SteamInference


def main():
    print("***Creation du moteur***")
    ihm = IhmSteamExpert()
    steam = SteamInference(ihm)
    print("***Ajout des regles***")
    steam.stringtorule("R1:Ordre=3=Quel est l'ordre?:Triangle/True")
    steam.stringtorule("R2:Triangle/True,Angle droit/True/La figure a-t-elle au moins un angle droit?:Triangle rectangle/True")
    steam.stringtorule("R3:Triangle/True,Cotes egaux=2=Conbien la figure a-t-elle de cotes egaux?:Triangle isocele/True")
    steam.stringtorule("R4:Triangle rectangle/True,Triangle isocele/True:Triangle rectangle isocele/True")
    steam.stringtorule("R5:Triangle/True,Cotes egaux=3=Conbien la figure a-t-elle de cotes egaux?:Triangle equilateral/True")
    steam.stringtorule("R6:Ordre=4=Quel est l'ordre?:Quatrilatere/True")
    steam.stringtorule("R7:Quatrilatere/True,Cotes paralleles=2=Conbien y a-t-il de cotes paralleles entre eux 0 ou 2 ou 4?:Trapeze/True")
    steam.stringtorule("R8:Quatrilatere/True,Cotes paralleles=4=Conbien y a-t-il de cotes paralleles entre eux 0 ou 2 ou 4?:Parallelograme/True")
    steam.stringtorule("R9:Parallelograme/True,Angle droit/True/La figure a-t-elle au moins un angle droit?:Rectangle/True")
    steam.stringtorule("R10:Parallelograme/True,Cotes egaux=4=Conbien la figure a-t-elle de cotes egaux?:Losange/True")
    steam.stringtorule("R11:Rectangle/True,Losange/True:Carre/True")
    print("***Resolution***")
    steam.solve()

if __name__ == "__main__":
    main()