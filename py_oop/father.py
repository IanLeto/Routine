
class person():


    def __init__(self, id=False, name=False, type=False):
        self.id = id
        self.name = name
        self.type = type

    def func(self):
        self.func2()

    def func2(self):
        print(self.name)

