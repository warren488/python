import sys
import math
from minterm import Minterm
from helpers import filter_input, initial_input_prompt


def main():
    print(sys.argv)
    minterms = input("enter your minterms seperated by a comma: ")
    filtered = filter_input(minterms)

    invalidterms = filtered[0]
    organizedminterms = filtered[1]
    largest = filtered[2]

    choice = initial_input_prompt(filtered[0], filtered[1])
    print(choice)

    while (choice == 'a') | (choice == 'd'):
        if choice == 'a':
            additions = input("enter list of terms")
            newly_filtered = filter_input(additions)
            invalidterms = newly_filtered[0]
            if largest < filtered[2]:
                largest = filtered[2]
            #below line causes duplication of terms
            organizedminterms += newly_filtered[1]
            choice = initial_input_prompt(invalidterms, organizedminterms)
        elif choice == 'd':
            deletions = input("list which terms you would like to delete")
            newly_filtered = filter_input(deletions)
            invalidterms = newly_filtered[0]
            if largest < filtered[2]:
                largest = filtered[2]
            for i in newly_filtered[1]:
                organizedminterms.remove(i)
            choice = initial_input_prompt(invalidterms, organizedminterms)
    
    binary_minterms = []
    organized_binary_minterms = {}
    number_of_digits = math.ceil(math.log10(largest)/math.log10(2))
    print("number of bits ",number_of_digits)
    largest_number_of_ones = -1
    for term in organizedminterms:
        push_on = Minterm(int(term))
        binary_minterms.append(push_on)
        if push_on.getOnes() > largest_number_of_ones:
            largest_number_of_ones = push_on.getOnes()
    
    for i in range(largest_number_of_ones):
        temp_ith_array = []
        for min in binary_minterms:
            if min.getOnes() == i:
                temp_ith_array.append(min)
        
        if len(temp_ith_array) > 0:
            organized_binary_minterms[i] = temp_ith_array

    for i in organized_binary_minterms:
        # The i in organized_binary_minterms just happened to be numbers because of use case, i seems to just take on the value of the key
        print(i,":")
        print(organized_binary_minterms[i][0].getImp())
        print(organized_binary_minterms[i][1].getImp())

    for i in range(largest_number_of_ones - 1):
        if organized_binary_minterms.has_key(i) & organized_binary_minterms.has_key(i+1):
            

    
        


if __name__ == "__main__": main()