try:
    result = 10/10
except ZeroDivisionError:
    print("Oops try to divide by zero.")

fruits = {
    "apple":5,
    "bananas":4,
    "orange":6
}

print(fruits["bananas"])


try:
    print(fruits["cherry"])

except KeyError:
    print("The key does not exist in dictionary")