class Animals:
    pass

class Pets(Animals):
    pass


class Dog(Pets):
    @staticmethod
    def Bark():
        print("Bow Bow")



d = Dog()
d.Bark()




