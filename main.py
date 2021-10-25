from Logic.CRUD import adaugVanzare
from Tests.allTests import runAllTests
from UI.console import runMenu



def main():
    runAllTests()
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista)
    lista = adaugVanzare("2", "Tabloul", "mister", 37, "none", lista)

    runMenu(lista)
if __name__ == '__main__':
    main()