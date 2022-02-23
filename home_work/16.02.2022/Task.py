# 11.01

class Dog(object):
    pass
if __name__ == "__main__":
    dog = Dog()

# 11.02

class Dog(object):
    t = 10
    b = 5
if __name__ == "__main__":
    tom = Dog()
    bob = Dog()
    print(tom.t)
    print(bob.b)

# 11.03

class Dog(object):
    def jump(self):
        print('Jump')
    def run(self):
        print('run')
if __name__ == "__main__":
    tom = Dog()
    bob = Dog()
    tom.jump()
    bob.run()

# 11.04

class Dog:
    def __init__(self, height, name, age):
        self.height = height
        self.name = name
        self.age = age
    def jump(self):
        print('Jump')
    def run(self):
        print('run')
    def bark(self):
        print('stop')
if __name__ == "__main__":
    dog = Dog(24, 'Bob', 8)
    dog.jump()
    dog.run()
    dog.bark()
    print(dog.name)
    print(dog.age)
    print(dog.height)

# 11.05

class Dog:
    def __init__(self, height, name, age):
        self.height = height
        self.name = name
        self.age = age
    def change_name(self, name):
        self.name = name
if __name__ == "__main__":
    dog = Dog(24, 'Bob', 8)
    dog.change_name('Tom')
    print(dog.name)
    print(dog.age)
    print(dog.height)

# 11.06

class Dog:
    def __init__(self, height, name, age, master):
        self.height = height
        self.name = name
        self.age = age
        self.__master = master
    def get_master(self):
        return self.__master
if __name__ == "__main__":
    dog = Dog(24, 'Bob', 8, 50)
    print(dog.get_master())
    print(dog.age)
    print(dog.height)

# 11.07

class Dog:
    def __init__(self, master="Minsk"):
        self.__master = master
    def get_master(self):
        return self.__master
    def set_master(self, master):
        self.__master = master
if __name__ == "__main__":
    dog = Dog()
    print(dog.get_master())
    dog.set_master('Brest')
    print(dog.get_master())

# 11.09

class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print("run")
    def jump(self):
        print("jump")
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print("sleep")
    def bark(self):
        print("bark")

class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print("run")
    def jump(self):
        print("jump")
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print("sleep")
    def meow(self):
        print("meow")

class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master
    def run(self):
        print("run")
    def jump(self):
        print("jump")
    def birthday(self):
        return self.age + 1
    def sleep(self):
        print("sleep")
    def fly(self):
        print("fly")
if __name__ == "__main__":
    dog = Dog("Bob", 10, "Tom")
    print(dog.name)
    cat = Cat("Tim", 3, "Jack")
    print(cat.master)
    parrot = Parrot("Bin", 12, "Ben")
    print(f'{parrot.age}, {parrot.birthday()}')

# 11.10

class Pet:
    def run(self):
        print("run")
    def jump(self):
        print("jump")
    def sleep(self):
        print("sleep")

class Dog(Pet):
    def bark(self):
        print("bark")

class Cat(Pet):
    def meow(self):
        print("meow")

class Parrot(Pet):
    def fly(self):
        print("fly")
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    parrot = Parrot()
    cat.sleep()
    cat.meow()
    cat.run()
    cat.jump()
    parrot.fly()
    dog.bark()


