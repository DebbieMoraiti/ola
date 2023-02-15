#   paixnidi petra-psalidi-xarti

epiloges = 'ΧΠΨΠΠΧΧΨΠΧΧΨΨΨΠΧΠΠΨΨ'
x = 0
active = True
while True:
    paiktis = input("Διάλεξε (Π)έτρα, (Ψ)αλίδι, (Χ)αρτί ή για να σταματήσεις πάτησε το space: ").upper()
    while paiktis not in ["π", "Π", "ψ", "Ψ", "χ", "Χ", " "] :
        if paiktis == " ":
            active = False
        else:
            paiktis = input("Έδωσες λάθος επιλογή, δώσε κάτι από (π,Π,ψ,Ψ,χ,Χ): ").upper()
            break
    # Επιλογή από τη προεπιλεγμένη σειρά χαρακτήρων
    computer = epiloges[x]
    if x == len(epiloges) - 1:
        x = 0
    else:
        x = x + 1
    #    Χρήστης και πρόγραμμα έχουν ίδια επιλογή
    if paiktis == computer:
        print("Ισοπαλία!")
    #   Ο χρήστης επέλεξε Πέτρα
    elif paiktis == "Π":
        if computer == "Χ":
            print("Έχασες :( ")
        elif epiloges == "Ψ":
            print("Με κέρδισες!")
    #   Ο χρήστης επέλεξε Χαρτί
    elif paiktis == "Χ":
        if computer == "Ψ":
            print("Έχασες :( ")
        elif computer == "Π":
            print("Με κέρδισες!")
    #   Ο χρήστης επέλεξε Ψαλίδι
    elif paiktis == "Ψ":
        if computer == "Π":
            print("Έχασες :( ")
        elif computer == "Χ":
            print("Με κέρδισες!")
print("Αντίο!")