import sys

def binary(number):
    if number <= 1:
        return [number]
    else:
        x = binary(number//2)
        x.append(number % 2)
        return x
        
if __name__ == "__main__": print(binary(int(sys.argv[1])))