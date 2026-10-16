from animal import Animal

class Parrot(Animal):

    def __init__(selfself,  name:str, age:int):
        super().__init__(name, age)

    def get_age_in_human_years(self) -> int:
        return self.get_age() * 5

    def express(self):
        print(f'{self.get_name()}: "Hello!"')
        print(r'''
    \
   (o>
\\_//)
 \_/_)
  _|_
    ''')

