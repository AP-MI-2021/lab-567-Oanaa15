from Logic.CRUD import adaugVanzare
from Tests.allTests import runAllTests
from UI.command_line_console import runMenu2
from UI.console import runMenu



def main():
    runAllTests()
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista)
    lista = adaugVanzare("2", "Tabloul", "mister", 37, "none", lista)

    print("Se doreste afisarea pe o line?")
    ok = input("Da raspuns(da/nu): ")
    if ok == "nu":
        runMenu(lista)
    else:
        runMenu2(lista, ok)

if __name__ == '__main__':
    main()