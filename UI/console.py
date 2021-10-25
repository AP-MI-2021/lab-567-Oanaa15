from Domain.vanzare import toString
from Logic.CRUD import adaugVanzare, stergVanzare, modifVanzare
from Logic.functionalitati import aplicDiscount


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Sterge vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare reducere - gold, silver sau none")
    print("a. Afisare vanzare")
    print("x. Iesire")

def uiAdaugaVanzare(lista):
    id = input("Dati id-ul: ")
    titlu = input("Dati titlul: ")
    gen = input ("Dati genul: ")
    pret = float(input("Dati pretul:"))
    reducere = input("Dati reducere:")
    return adaugVanzare(id, titlu, gen, pret, reducere, lista)

def uiStergeVanzare(lista):
    id = input("Dati id-ul vanzarii de sters: ")
    return stergVanzare(id, lista)

def uiModificaVanzare(lista):
    id = input("Dati id-ul: ")
    titlu = input("Dati titlul: ")
    gen = input("Dati genul: ")
    pret = float(input("Dati pretul:"))
    reducere = input("Dati reducere:")
    return modifVanzare(id, titlu, gen, pret, reducere, lista)

def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))

def uiAplicDiscount(lista):
    return aplicDiscount(lista)

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaVanzare(lista)
        elif optiune == "2":
            lista = uiStergeVanzare(lista)
        elif optiune == "3":
            lista = uiModificaVanzare(lista)
        elif optiune == "4":
            lista = uiAplicDiscount(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")