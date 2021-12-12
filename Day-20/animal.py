class Animal:
    def __init__(self):
        self.eyes = 2
    
    def breathing(self):
        print("I am breathing")
    
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathing(self):
        super().breathing()
        print("Under the water")

    def swimming(self):
        print("I am swimming")

nemo = Fish()
nemo.swimming()
nemo.breathing()