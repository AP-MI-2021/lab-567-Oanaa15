from Domain.vanzare import getPret, getGen
from Logic.CRUD import adaugVanzare, getById
from Logic.functionalitati import aplicDiscount, modifGenDupaTitlu


def testAplicDiscount():
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista)

    lista = aplicDiscount(lista)

    assert getPret(getById("1", lista)) == 13.5
    assert getPret(getById("2", lista)) == 19

def testModifGenDupaTitlu():
    lista =[]
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista)

    titlu = "Tabloul"
    genNou = "crima"

    lista = modifGenDupaTitlu(lista, titlu, genNou)

    assert getGen(getById("2",lista)) == genNou
    assert getGen(getById("1",lista)) == "clasica"

