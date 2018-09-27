from Implicant import Implicant


def filter_input(minterms):
    largest = -1
    minterms = minterms.split(',')
    for i in range(len(minterms)):
        minterms[i] = minterms[i].strip()
    organizedminterms = []
    invalidterms = []
    for term in minterms:
        if (term.isdigit() is False):
            invalidterms.append(term)
        elif (int(term) < 0):
            invalidterms.append(term)
        elif organizedminterms.count(term) == 0:
            organizedminterms.append(term)
            if int(term) > largest:
                largest = int(term)

    
    return [invalidterms, organizedminterms, largest]

def initial_input_prompt(invalidterms, organizedminterms):
    if len(invalidterms) > 0:        
        print("the following list of terms entered are invalid ",invalidterms)
    
    print("The program will now operate on the following terms ",organizedminterms)
    input()
    choice = input("If you wish to add any terms enter 'a' \nif you wish to delete terms enter 'd' \nor press enter to continue")
    return choice

def compare(term1, term2):
    count = 0
    i1 = term1.getImp()
    i2 = term2.getImp()

    for i in range(len(i2)):
        if i2[i] != i1[i]:
            count += 1
            diff = i
        if count > 1:
            return -1
    
    return diff

def mainloop(num_ones, bin_terms):

    essentian_PI = []
    # matched_groups = []
    Implicants = {0:"start"}
    while len(Implicants.keys()) > 0:
        Implicants = {}
        for i in range(num_ones+1):
            if not i in bin_terms:
                continue

            temp_list = []
            if (i in bin_terms) & ((i+1) in bin_terms):
                print("we got {} and {}".format(i, i+1))
                # matched_groups.append(i)
                for mint in bin_terms[i]:
                    for com_mint in bin_terms[i+1]:
                        diff = compare(mint, com_mint)
                        if diff > -1:
                            mint.toggleMatched()
                            com_mint.toggleMatched()
                            temp_list.append(Implicant(mint, com_mint, diff))

                    if not mint.isMatched():
                        essentian_PI.append(mint)
            
            else:
                for mint in bin_terms[i]:
                    if not mint.isMatched():
                        essentian_PI.append(mint)            

            if len(temp_list) > 0:
                Implicants[i] = temp_list

        bin_terms = Implicants

        for i in Implicants:
            print("in func")
            print(i,":")
            for imp in Implicants[i]:
                print(imp.getImp())
    for mint in essentian_PI:
        print(mint.getImp())
    return essentian_PI