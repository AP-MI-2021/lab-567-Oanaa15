from Domain.vanzare import getPret
from Logic.CRUD import adaugVanzare, getById
from Logic.functionalitati import aplicDiscount


def testAplicDiscount():
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista)

    lista = aplicDiscount(lista)

    assert getPret(getById("1", lista)) == 13.5
    assert getPret(getById("2", lista)) == 19
