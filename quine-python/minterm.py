from binary import binary

class Minterm:
    def __init__(self, decimal):
        self.matched = False
        self.ones = 0
        self.minterm = decimal
        # MUST GET A BINARY TO DECIMAL CONVERTER
        self.bin = binary(decimal)
        self.essential = False

        for x in self.bin:
            if x == 1:
                self.ones += 1

    def getOnes(self):
        return self.ones

    def isMatched(self):
        return self.matched

    def getMin(self):
        return self.minterm

    def toggleMatched(self):
        self.matched = True
        return

    def isEssential(self):
        return self.essential 

    def getImp(self):
        return self.bin
    
def main():
    x = Minterm(38, 5)
    print(x.getImp())
    print(x.getMin())
    print(x.getOnes())
if __name__ == "__main__": main()