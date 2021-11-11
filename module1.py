def arithmetic(a: float,b:float, c:str):
    """Lihtne kalkulaator
    + - liitumine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype float:
    """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("Viga")
        r=0.0
    return  r

#Visokosnqi god-liigaasta

def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab True kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsiooni vastusloogilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus

#Tehingud ruuduga

def square(a=float):
    """Ruudu külg
    P=ümbermõõt
    S=pindala
    d=diagonaal
   :param float a: Ruudu külg
   :rtype float:
   """
vas=() 
   from math import*
   if vas=="P":
       P=a*4
   elif vas=="S":
       S=a**
   elif vas=="di"
       di=a*sqrt(2)
     round(di,2))
   else:
       print("Viga")

    return P, S, di

       
