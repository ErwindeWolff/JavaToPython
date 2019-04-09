from math import sqrt

def powerset(listt):
    powerset = [[]]
    for element in listt:
        powerset += [sett + [element] for sett in powerset]
    return powerset

print(powerset(["A", "B", "C"]))




def is_prime(number):
    return len([x for x in range(2, int(sqrt(number))+1) if number%x == 0]) == 0


for x in range(2, 100):
    if (is_prime(x)):
        print(x)
