#2
def generate_array (length , start ):
    array= []
    for i in range(length):
        array.append(start)
        start+=1
    return array

print(generate_array(10 , 2))