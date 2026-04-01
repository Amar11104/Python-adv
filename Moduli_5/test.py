def get_even_numbers():
    total = 0
    for i in range(1,11):
        if i % 2 == 0:
            total = total + i
    return total

print(get_even_numbers())