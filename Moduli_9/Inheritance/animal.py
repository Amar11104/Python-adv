class Animal:
    def sound(self):
        print("Some generiic animal sound.")

class Dog(Animal):

     def sound(self):
         print("WOOF! WOOF!")

class Cat(Animal):
    def sound(self):
        print("Meow Meow")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

