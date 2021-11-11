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

#Tehingud ruuduga
def kvadrat():

result=square(int(input("Введите сторону квадрата: ")))
print (result)


#Aastaaeg

def season(kuu):
   if mesyac in [12, 1, 2]:
       print("Зима")
   elif mesyac in [3, 4, 5]:
       print("Весна")
   elif mesyac in [6, 7, 8]:
       print("Лето")
   elif mesyac in [9, 10, 11):
       print("Осень")
   else:
       print("Viga")

       print("Neverno vveden nomer msyaca!")

n = int(input("Введите номер месяца (1-12): "))

season(n)
