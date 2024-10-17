import random

def feladatlista():
    fejiras = []
    for i in range(0,10,1):
        fvi = float(random.random())
        if fvi < 0.5:
            fejiras.append("fej")
        else:
            fejiras.append("íras")
    return fejiras

def feladat4(fejiras):
    i = 0
    fejek = 0
    irasok = 0
    while i < len(fejiras):
        if fejiras[i] == "fej":
            fejek += 1
        else:
            irasok += 1
        i += 1
    print(f"fejek száma: {fejek}")
    print(f"írások száma: {irasok}")

def feladatdobasok():
    i = 0
    lista = []
    while i < 200:
        dobasok = int(random.random()*7)
        lista.append(dobasok)
        i += 1
    return lista

def feladat5_1(dobasok):
    i = 0
    egy = 0
    ketto = 0
    harom = 0
    negy = 0
    ot = 0
    hat = 0
    while i < len(dobasok):
        if dobasok[i] == 1:
            egy += 1
        elif dobasok[i] == 2:
            ketto += 1
        elif dobasok[i] == 3:
            harom += 1
        elif dobasok[i] == 4:
            negy += 1
        elif dobasok[i] == 5:
            ot += 1
        else:
            hat += 1
        i += 1
    print(f"1-est dobtunk {egy} alkalommal")
    print(f"2-est dobtunk {ketto} alkalommal")
    print(f"3-ast dobtunk {harom} alkalommal")
    print(f"4-est dobtunk {negy} alkalommal")
    print(f"5-öst dobtunk {ot} alkalommal")
    print(f"6-ost dobtunk {hat} alkalommal")

def feladat5_2(dobasok):
    i = 0
    dobas = [0,0,0,0,0,0]
    while i < len(dobasok):
        dobas[i] += 1
        i += 1
    for p in range(0,6,1):
        p += 1
        print(f"{p}. dobtunk {dobas[i]} alkalommal")

def feladat5_3(dobasok, szam):
    i = 0
    szam2 = 0
    for o in range(0,6,1):
        while i < len(dobasok):
            if dobasok[i] == szam:
                szam2+=1
            i += 1
    return szam2

def feladatcinkelt():
    i = 0
    dobasok = []
    while i < 200:
        dob = float(random.random())
        if dob >= 0.6:
            dobasok.append(6)
        elif (dob < 0.6) and (dob >= 0.5):
            dobasok.append(5)
        elif (dob < 0.5) and (dob >= 0.4):
            dobasok.append(4)
        elif (dob < 0.4) and (dob >= 0.3):
            dobasok.append(3)
        elif (dob < 0.3) and (dob >= 0.2):
            dobasok.append(2)
        else:
            dobasok.append(1)
        i += 1
    return dobasok

def feladat6(dobasok, szam):
    i = 0
    szam2 = 0
    for o in range(0,6,1):
        while i < len(dobasok):
            if dobasok[i] == szam:
                szam2+=1
            i += 1
    return szam2