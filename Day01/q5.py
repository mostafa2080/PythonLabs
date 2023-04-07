#5
def reverse_string(string):
    return string[::-1]


print(reverse_string("hello")) 


def reverse_string2(string):
    reversed_str = ""
    for i in range(len(string)-1, -1, -1):
        reversed_str += string[i]
    return reversed_str

print(reverse_string("mostafa")) 
