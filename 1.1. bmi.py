
#zadanie 1.1.
#bmi

m = float(input("podaj masę ciała w kg: "))
h = float(input("podaj wzrost w m: "))
bmi = m/(h**2)
print (bmi)
if bmi<18.5:
    print("niedowaga") 
elif bmi<25:
    print("waga w normie")
elif bmi<30:
    print("nadwaga")
elif 30<bmi:
    print("otyłość")
