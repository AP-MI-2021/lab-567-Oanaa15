def creeazaVanzare(id, titlu, gen, pret, reducere):
    '''
    creeaza un dictionar ce retine o vanzare de carte
    :param id: id-ul unei vanzari - string
    :param titlu: titlul unei carti - string
    :param gen: genul unei carti - string
    :param pret: pretul unei carti - float
    :param reducere: tip reducere client(none, silver sau gold) - string
    :return: un dictionar ce retine o vanzare de carte
    '''
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere

    }
def getId(vanzare):
    '''
    da id-ul vanzarii
    :param vanzare: un dictionar de tip vanzare
    :return: id-ul vanzarii - string
    '''
    return vanzare["id"]

def getTitlu(vanzare):
    '''
    da titlul cartii
    :param vanzare: un dictionar de tip vanzare
    :return: titlul cartii - string
    '''
    return vanzare["titlu"]

def getGen(vanzare):
    '''
    da genul cartii
    :param vanzare: un dictionar de tip vanzare
    :return: genul cartii - string
    '''
    return vanzare["gen"]

def getPret(vanzare):
    '''
    da pretul cartii
    :param vanzare: un dictionar de tip vanzare
    :return: pretul cartii - float
    '''
    return vanzare["pret"]

def getReducere(vanzare):
    '''
    da tipul de reducere - none, silver sau gold
    :param vanzare: un dictionar de tip vanzare
    :return: tipul de reducere al unui client
    '''
    return vanzare["reducere"]

def toString(vanzare):
    '''

    :param vanzare:
    :return:
    '''
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere: {}".format(
        getId(vanzare),
        getTitlu(vanzare),
        getGen(vanzare),
        getPret(vanzare),
        getReducere(vanzare)
    )