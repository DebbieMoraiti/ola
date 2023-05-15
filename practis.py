n = 10
vhma = 00
x = 0
y = 0
while vhma != " ":
    vhma = (input("Δώστε αριθμό βημάτων και κίνηση πάνω, κάτω, αριστερά, δεξία. Πχ. r7, ή κενό χαρακτήρα για τερματισμό: "))
    while vhma[0] not in ["u", "U", "d", "D", "r", "R", "L", "l"] and not vhma[1].isdigit():
        print("Έδωσες λάθος επιλογή, δώσε κάτι από (u,d,r,l).")
        break

    arithmos = int(vhma[1])
    kinisi = str(vhma[0])
    thesi = (0,0)
    if kinisi == "u":
        x = x - arithmos
        print(x)
        if x < 0 or x >= n:
            print("ΣΦΑΛΜΑ! Κίνηση έξω από τα όρια του χώρου")
            x = x + arithmos
        else:
            print("Η νέα θέση του ρομπότ είναι: (" + str(x) + ", " + str(y) + ")")
    if kinisi == "d":
        x = x + arithmos
        print(x)
        if x < 0 or x >= n:
            print("ΣΦΑΛΜΑ! Κίνηση έξω από τα όρια του χώρου")
            x = x - arithmos
        else:
            print("Η νέα θέση του ρομπότ είναι: (" + str(x) + ", " + str(y) + ")")
    if kinisi == "r":
        y = y + arithmos
        print(y)
        if y < 0 or y >= n:
            print("ΣΦΑΛΜΑ! Κίνηση έξω από τα όρια του χώρου")
            y = y - arithmos
        else:
            print("Η νέα θέση του ρομπότ είναι: (" + str(x) + ", " + str(y) + ")")
    if kinisi == "l":
        y = y - arithmos
        print(y)
        if y < 0 or y >= n:
            print("ΣΦΑΛΜΑ! Κίνηση έξω από τα όρια του χώρου")
            y = y + arithmos
        else:
            print("Η νέα θέση του ρομπότ είναι: (" + str(x) + ", " + str(y) + ")")


    #up x = x - vhma[1]
    #down x = x + vhma[1]
    #left y = y - vhma[1]
    #right y = y + vhma[1]
