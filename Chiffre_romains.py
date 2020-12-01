VAL_ROM = [ "M", "CM", "D", "CD", "C", "XC",
            "L", "VL", "XL", "X", "IX", "V", "IV", "I" ]
VAL_INT = [ 1000, 900, 500, 400, 100, 90,
        50, 45, 40, 10, 9, 5, 4, 1 ]
def int2rom(val):
    remainder=val
    retour_romain=''
    if val<1 or val>3999: return "ERROR"
    for compteur in range(len(VAL_INT)):
        while remainder>=VAL_INT[compteur]:
            retour_romain+=VAL_ROM[compteur]
            remainder -= VAL_INT[compteur]
    return retour_romain
def rom2int(s):
    index=0
    retour_int=0
    for compteur in range(len(VAL_ROM)):
        sRom= VAL_ROM[compteur]
        lensRom=len(sRom)
        while s[index:index+lensRom]==sRom:
            retour_int += VAL_INT[compteur]
            index += lensRom
    if int2rom(retour_int)!="ERROR":
        return retour_int
    else: return "ERROR"

def div( ch1 , ch2 ):
    return ch1 / ch2
def somme( ch1 , ch2 ):
    return ch1 + ch2
def sous( ch1 , ch2 ):
    return ch1 - ch2
def mul( ch1 , ch2 ):
    return ch1*ch2
def calc_rom(opp, ch1, ch2):
    ch1=rom2int(ch1)
    ch2=rom2int(ch2)
    if(ch1=='ERROR'):
        return ch1
    if(ch2=='ERROR'):
        return ch2
    if(opp == "+"):
        res=somme(ch1, ch2)
        res=int2rom(res)
        return res
    elif(opp=="*"):
        res=mul(ch1, ch2)
        res=int2rom(res)
        return res
    elif(opp=="/"):
        res=div(ch1 , ch2)
        res=int2rom(res)
        return res
    elif(opp=="-"):
        res=sous(ch1, ch2 )
        res=int2rom(res)
        return res

