class Animal:

    def talk(self):
        print('Animal sounds')


class Dog(Animal):

    def talk(self):
        print('woof woof')


class Cat(Animal):

    def talk(self):
        print('meow meow')


def animal_talk(animal):
    animal.talk()


dog = Dog()
cat = Cat()

animal_talk(dog)
animal_talk(cat)
