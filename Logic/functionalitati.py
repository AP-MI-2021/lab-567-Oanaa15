from Domain.vanzare import getReducere, creeazaVanzare, getId, getTitlu, getGen, getPret


def aplicDiscount(lista):
    '''
    aplica un discount de 5% pentru reduceri silver, 10% pentru reducerile gold
    :param lista: o lista de vanzari
    :return: lista in care sunt aplicate reducerile corespunzatoare
    '''
    listaNoua = []
    for vanzare in lista:
        pret = getPret(vanzare)
        if getReducere(vanzare) == "silver":
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                getGen(vanzare),
                getPret(vanzare) - pret * 5/100,
                getReducere(vanzare)
            )
            listaNoua.append(vanzareNoua)
        elif getReducere(vanzare) == "gold":
                vanzareNoua = creeazaVanzare(
                    getId(vanzare),
                    getTitlu(vanzare),
                    getGen(vanzare),
                    getPret(vanzare) - pret * 10 / 100,
                    getReducere(vanzare)
                )
                listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

def modifGenDupaTitlu(lista, titlu, genNou):
    '''
    modifica genul pentru un titlu dat
    :param lista: o lista de vanzari
    :param titlu: titlul dat
    :return: lista cu genurile modificate pentru titlul dat
    '''
    listaNoua =[]
    for vanzare in lista:
        if getTitlu(vanzare) == titlu:
            vanzareNoua = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                getGen(vanzare),
                getPret(vanzare),
                getReducere(vanzare)
            )
            vanzareNoua[2] = genNou
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua

def pretMinimGen(lista):
    '''
    determina pretul minim pentru fiecare gen
    :param lista: o lista de vanzari
    :return: fiecare gen cu pretul minim
    '''
    listaNoua = {}
    for vanzare in lista:
        pret = getPret(vanzare)
        gen = getGen(vanzare)
        if gen in listaNoua:
            if pret < listaNoua[gen]:
                listaNoua[gen] = pret
        else:
            listaNoua[gen] = pret
    return listaNoua


def ordonareListaDupaPret(lista):
    '''
    ordoneaza crescator vanzarile dupa pret
    :param lista: o lista de vanzari
    :return: lista de vanzari ordonata crescator dupa pret
    '''
    return sorted(lista, key=lambda vanzare: getPret(vanzare))







