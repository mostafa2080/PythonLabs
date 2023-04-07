#3
array = []
for i in range(5):
    num = int(input("Enter an integer: "))
    array.append(num)

desc_array = sorted(array, reverse=True)

asc_array = sorted(array)

print("Original array:", array)
print("Descending order:", desc_array)
print("Ascending order:", asc_array)