import random
raten=random.randint(0,1000)
versuch=int(input("gib eine zahl ein"))
while raten != versuch:
    if versuch>raten+100:
        print("viel zu hoch")
    elif versuch>raten:
        print("zu hoch")
    elif versuch<raten-100:
        print("viel zu tief")
    else:
        print("zu tief")
    versuch=int(input("gib eine zahl ein"))#
print("richtig")    