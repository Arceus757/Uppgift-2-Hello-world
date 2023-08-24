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
print ( "Du är redan " + Age + " år gammal, dags att flytta från dina föräldrar!")

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






