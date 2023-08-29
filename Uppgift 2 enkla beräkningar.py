#1. Kommentarer i Python (använd # för en enskild kommentar eller ‘‘‘ för flera rader av kommentarer) 

#2 Enkla beräkningar 
x = 5
y = 15
c = x + y 
print( c )

#3. Bygg vidare på välkomstprogrammet med att be om deras ålder
Name = input( "Ange ditt namn: ")
Age = input( "Ange din ålder: ")
print ( "Hej "  + Name + "!")
print ( "Du är redan " + Age + " år gammal dags att flytta från dina föräldrar!")

#4. Gör en miniräknare som multiplicerar två olika tal som användaren matar in
What = input("Sugen på att multiplicera två olika tal? :  ")

a = float( input("Ange första talet: ") )
b = float( input("Ange andra talet: ") )

if What == "ja":
    c = a * b
    print("Svar: " + str(c))

elif What == "nej": 
    print ("vrf fortsätter du att räkna? du svarade ju nej")


else:
    print ("man får bara svara ja eller nej")

#5. BMI-kalkylator - du ska göra en räknare som beräknar BMI (Vikt / Längd ^ 2)
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Ange din vikt i kilogram: "))
height = float(input("Ange din längd i meter: "))

bmi = calculate_bmi(weight, height)
print("Ditt BMI är:", bmi)

#6. ”Livet i veckor” - kolla hur länge användaren har levt i veckor
age = int(input("Ange din ålder igen: "))
weeks = age * 52
print("Du har levt i", weeks, "veckor.")

#7. Vikträknare (från kg till lbs)
weight_kg = float(input("Ange vikten i kilogram för att se din vikt i pounds: "))
weight_lbs = weight_kg * 2.20462
print("Vikten i pounds är:", weight_lbs)







