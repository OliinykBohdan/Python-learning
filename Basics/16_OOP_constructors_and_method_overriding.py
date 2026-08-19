class Robot:
    name = None
    age = None
    combat = None

    def __init__(self, name='C-3PO', age=10, combat=False):
        self.set_data(name, age, combat)
        self.get_data()

    def set_data(self, name, age, combat):
        self.name = name
        self.age = age
        self.combat = combat

    def get_data(self):
        print('Name:', self.name, 'Age:', self.age, 'Combat:', self.combat)


robot1 = Robot(age=20)
robot2 = Robot('C-3PO', 10, False)
