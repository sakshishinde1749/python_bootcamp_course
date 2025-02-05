class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()      #inheriting from parent class

    # changing the parents class function
    def breathe(self):
        super().breathe()
        print("doint this underwater")

    def swim(self):
        print("fish swims")