

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

def delete(original, deletions):
    for i in deletions:
        original.remove(i)