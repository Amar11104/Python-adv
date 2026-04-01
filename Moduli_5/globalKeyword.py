def greet(name):
    global message
    message = f"Hello, {name}"
    print(message)



greet("Jona")

print(message)