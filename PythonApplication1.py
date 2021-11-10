from module1 import*
while True:
    print("Funktsioonid".center(50,"+"))
    v=input("arithmetic-A")
    if v.upper()=="A":
        arv1=float(input("Arv1:"))
        arv2=float(input("Arv2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta: ")))
        print(rezult)