from Domain.vanzare import getId, getTitlu, getGen, getPret, getReducere
from Logic.CRUD import adaugVanzare, getById, stergVanzare, modifVanzare


def testAdaug():
    lista = adaugVanzare("1", "Harry Potter", "fictiune", 30, "silver", [])

    assert getId(lista[0]) == "1"
    assert getTitlu(lista[0]) == "Harry Potter"
    assert getGen(lista[0]) == "fictiune"
    assert getPret(lista[0]) == 30
    assert getReducere(lista[0]) == "silver"


def testGetById():
    lista = []
    lista = adaugVanzare("1", "Harry Potter", "fictiune", 30, "silver", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitlu(getById("1", lista)) == "Harry Potter"
    assert getGen(getById("1", lista)) == "fictiune"
    assert getPret(getById("1", lista)) == 30
    assert getReducere(getById("1", lista)) == "silver"

def testStergVanzare():
    lista = []
    lista = adaugVanzare("1", "Harry Potter", "fictiune", 30, "silver", lista)
    lista = adaugVanzare("2", "Dune", "actiune", 45, "none", lista)

    lista = stergVanzare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

def testModifVanzare():
    lista = []
    lista = adaugVanzare("1", "Harry Potter", "fictiune", 30, "silver", lista)
    lista = adaugVanzare("2", "Dune", "actiune", 45, "none", lista)

    lista = modifVanzare("1", "Harry Potter vol. 1", "fictiune si magie", 15, "silver", lista)
    lista = modifVanzare("2", "Dune", "SF", 35, "none", lista)

    assert getId(lista[0]) == "1"
    assert getGen(lista[0]) == "fictiune si magie"
    assert getTitlu(lista[0]) == "Harry Potter vol. 1"
    assert getPret(lista[0]) == 15
    assert getReducere(lista[0]) == "silver"
    assert getGen(lista[1]) == "SF"














