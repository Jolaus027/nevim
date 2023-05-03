slovo = ["s","a","m","o"]
slovo_hadaj = ["","","",""]
count = 0
Vyra = False
while count < 10 and Vyra == False:
    hadaj = input("Zadaj pismenko: ")
    if hadaj in slovo:
        
        print("ano")
        print(slovo.index(hadaj)+1)
        slovo_hadaj[slovo.index(hadaj)] = hadaj

    elif slovo_hadaj[0] == "s" and slovo_hadaj[1] == "a" and slovo_hadaj[2] == "m" and slovo_hadaj[3] == "o":

        Vyra = True

    else:

        print("nie")
        count += 1


print(slovo_hadaj)

if count >= 10 :
    
    print("Uz nemas pokusy")

else:

    print("Vyhral si")

