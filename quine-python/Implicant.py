from minterm import Minterm

class Implicant:
    def __init__(self, imp1, imp2, bit_dif):
        self.matched = False
        self.minterms = []
        self.bin = imp1.getImp()
        self.bin[bit_dif] = -1
        self.ones = imp1.getOnes()
        self.essential = False
        if(isinstance(imp1, Implicant) & isinstance(imp2, Implicant)):
            mins2 = imp2.getMins()
            mins1 = imp1.getMins()
            for i in range(len(mins1)):
                self.minterms.append(mins1[i])
                self.minterms.append(mins2[i])


        if(isinstance(imp1, Minterm) & isinstance(imp2, Minterm)):
            self.minterms.append(imp1.getMin())
            self.minterms.append(imp2.getMin())

    def check(self, checkfor):
        for i in checkfor:
            check = i.getImp()
            found = True
            for c in range(len(check)):
                if check[c] != self.bin[c]:
                    found = False
                if found: return True
        return False

    def getOnes(self):
        return self.ones

    def isMatched(self):
        return self.matched

    def getMins(self):
        return self.minterms

    def toggleMatched(self):
        self.matched = True
        return

    def isEssential(self):
        return self.essential 

    def getImp(self):
        return self.bin

