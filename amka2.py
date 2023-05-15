# προσδιορισμός ηλικία, φύλου βάση του ΑΜΚΑ
paiktis = "N"
while paiktis != "Ο" or "ο":
    # ελέγχω αν είναι 11 τα ψηφία που έδωσε και προτρέπω να ξαναδώσει σωστό αριθμό εφόσον δεν είναι 11
    amka = input("Πληκτρολογήστε τον 11ψήφιο αριθμό ΑΜΚΑ σας: ")
    while len(amka) != 11:
        amka = input("Παρακαλώ δώστε 11 ψηφία: ")
    etos_gennisis = 0
    ilikia = 0
    dekaetia = int(amka[4])
    xronos = int(amka[5])

    # ελέγχω αν έχουν γεννηθεί μετά το 2000 για να φτιαξω το έτος γέννησης με 4 ψηφία και όχι 2 όπως είναι για να μπορεί
    # να γίνει η αφαίρεση από το 2022 σωστά
    if dekaetia <= 2:
        etos_gennisis = 2000 + (dekaetia * 10) + xronos
        print(etos_gennisis)
        ilikia = 2022 - etos_gennisis
    else:
        etos_gennisis = 1900 + (dekaetia * 10) + xronos
        print(etos_gennisis)
        ilikia = 2022 - etos_gennisis
    print("Η ηλικία σας είναι: ", ilikia)

    # ελέγχει αν το δεύτερο μέρος του ΑΜΚΑ είναι άρτιος ή περιττός, ώστε να
    # προσδιορίζει το φύλο

    if int(amka[-1]) % 2 == 0:
        print("Είστε κοριτσάκι.")
    else:
        print("Είστε αγοράκι.")
    eksodos = input("Θέλετε να ελέγξετε άλλο ΑΜΚΑ; (Ν)αι / (Ό)χι:").upper()
    while eksodos not in ["ο", "Ο", "ν", "Ν"]:
        eksodos = input("Έδωσες λάθος επιλογή, πληκτρολόγησε Ν για να συνεχίσεις, Ο για να σταματήσουμε: ").upper()
