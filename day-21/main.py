"""day-21"""


class Animal:
    """Animal"""
    def __init__(self, name):
        self.num_eyes = 2
        self.name = name

    def breathe(self):
        """breathe"""
        print("Inhale, exhale.")


class Fish(Animal):
    """Fish"""
    def __init__(self):
        super().__init__("Dalei")

    def breathe(self):
        """breathe"""
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        """swim"""
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
print(nemo.name)
