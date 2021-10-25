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



