import sys
from minterm import Minterm
from helpers import filter_input, initial_input_prompt


def main():
    print(sys.argv)
    minterms = input("enter your minterms seperated by a comma: ")
    filtered = filter_input(minterms)

    invalidterms = filtered[0]
    organizedminterms = filtered[1]

    choice = initial_input_prompt(filtered[0], filtered[1])
    print(choice)

    while (choice == 'a') | (choice == 'd'):
        if choice == 'a':
            additions = input("enter list of terms")
            newly_filtered = filter_input(additions)
            invalidterms = newly_filtered[0]
            #below line causes duplication of terms
            organizedminterms += newly_filtered[1]
            choice = initial_input_prompt(invalidterms, organizedminterms)
        elif choice == 'd':
            deletions = input("list which terms you would like to delete")
            newly_filtered = filter_input(deletions)
            invalidterms = newly_filtered[0]
            for i in newly_filtered[1]:
                organizedminterms.remove(i)
            choice = initial_input_prompt(invalidterms, organizedminterms)
    
    binary_minterms = []
    for term in organizedminterms:
        binary_minterms.append(Minterm(int(term)))
    
    for min in binary_minterms:
        print(min.getImp())


if __name__ == "__main__": main()