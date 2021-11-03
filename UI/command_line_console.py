from Logic.CRUD import adaugVanzare, stergVanzare
from UI.console import showAll, runMenu


def oneLine(lineCom, lista):
    lineCom = lineCom.spit(";")
    i = 0
    while (i < lineCom):
        if lineCom[i] == "add":
            lista = adaugVanzare(lineCom[i+1], lineCom[i+2], lineCom[i+3], lineCom[i+4], lineCom[i+5])
            i += 5
        elif lineCom[i] == "delete":
            lista = stergVanzare(lineCom[i+1], lista)
            i +=1
        elif lineCom[i] == "showall":
            showAll(lista)
    return lista

def UiOneLine(lista):
    lineCom = input("Dati comenzile potrivite: ")
    return oneLine(lineCom, lista)

def printMeniu2():
    print("1. Adauga o vanzare/Sterge o vanzare/Arata toate vanzarile: ")
    print("x. Iesire")

def runMenu2(lista, ok):
    while True:
        printMeniu2()
        optiune = input("Alegeti optiune: ")
        if optiune == "1":
            lista = UiOneLine(lista)
        elif optiune == "back":
            ok = "nu"
            print("Schimbam interfata")
            runMenu(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")








