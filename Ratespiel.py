import random
import time
while True:
    auswahl = ["SCHERE","STEIN","PAPIER"]
    computerauswahl = random.choice(auswahl)
    print("Willkommen zu meinem Schere Stein Papier spiel das sind die optionen\n-Schere\n-Stein\n-Papier\ngib deine Wahl hier ein:")
    text=input()
    userEingabe=text.upper()
    if userEingabe == "SCHERE" or userEingabe == "STEIN" or userEingabe == "PAPIER":
        print("  ")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("  ")
        if userEingabe == "SCHERE" and computerauswahl == "PAPIER":
            print("du hast gewonnen")
            print("weil du schere hast und der computer Papier")
        elif userEingabe == "STEIN" and computerauswahl == "SCHERE":
            print("du hast gewonnen")
            print("weil du Stein hast und der computer Schere")
        elif userEingabe == "PAPIER" and computerauswahl == "STEIN":
            print("du hast gewonnen")
            print("weil du Papier hast und der computer Stein")
        elif userEingabe == computerauswahl:
            print("Unentschieden")
            print("weil du",userEingabe,"hast und der computer auch",computerauswahl,"hat")
        else:
            print("du hast verloren")
            print("weil du",userEingabe,"hast und der computer",computerauswahl,)
    else:
        print("dieses Eingabe ist nicht richtig!")
    time.sleep(2)
    print("Wenn du nochmal spielen willst dann drück [y] und wenn nicht [n]")
    V=input()
    V2=V.upper()
    if V2 != "Y":
        break