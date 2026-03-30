names = ["Don","Orges","Gjin","Amar","Orik"]

for name in names:
    print(name)

sentance = "Hello, World"

for char in sentance:
    if char.isalpha():
        print(char)

for num in range(1, 6):
    print(num)

numbers = [12,13,17,22,55,105,100]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"The maximum value in the list is: ", maximum)
























