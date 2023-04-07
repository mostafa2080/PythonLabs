#4
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0: 
        return "fizz"
    elif num % 5 == 0: 
        return "buzz"
    else:
        return "Number is Not Divivdable by 3 or 5"



print(fizzbuzz(11))