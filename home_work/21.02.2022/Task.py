class Pet:
    def __init__(self, name):
        self.name = name
    def name(self):
        return self.name

class Cat(Pet):
    @classmethod
    def cat(cls):
        print('Мяу')

class Dog(Pet):
    @classmethod
    def dog(cls):
        print('Гав')

if __name__ == "__main__":
    pet = Pet(input('enter name pet: '))
    print(pet.name)
    Cat.cat()
    Dog.dog()
