from Tests.testCRUD import testAdaug, testGetById, testStergVanzare, testModifVanzare
from Tests.testDomeniu import testVanzare
from Tests.testFunctionalitati import testAplicDiscount, testModifGenDupaTitlu, testPretMinimGen, \
    testOrdonareListaDupaPret


def runAllTests():
    testVanzare()
    testAdaug()
    testGetById()
    testStergVanzare()
    testModifVanzare()
    testAplicDiscount()
    testModifGenDupaTitlu()
    testPretMinimGen()
    testOrdonareListaDupaPret()