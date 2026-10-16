from parrot import Parrot
from turtle import Turtle
from person import Person

if __name__ == "__main__":

    kesha = Parrot("Kesha", 2)
    zavala = Turtle("Zavala", 4)

    kesha.happy_birthday()

    jack = Person("Jack", kesha)
    john = Person("John")

    print("Информация о Джеке:")
    jack.get_pet_info()

    print("\nИнформация о Джоне (до заведения питомца):")
    john.get_pet_info()

    john.set_pet(zavala)

    print("\nИнформация о Джоне (после заведения питомца):")
    john.get_pet_info()