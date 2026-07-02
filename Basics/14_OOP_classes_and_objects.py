# Task 1

print('-' * 10, 'Task 1:', sep='\n')


class Robot:
    name = None
    age = None
    combat = None

    def set_data(self, name, age, combat):
        self.name = name
        self.age = age
        self.combat = combat

    def get_data(self):
        print('Name:', self.name, 'Age:', self.age, 'Combat:', self.combat)


robot1 = Robot()
robot1.set_data('R2-D2', '20', False)
# robot1.name = 'R2-D2'
# robot1.age = 20
# robot1.combat = False

robot2 = Robot()
robot2.set_data('C-3PO', '10', False)
# robot2.name = 'C-3PO'
# robot2.age = 10
# robot2.combat = False

robot1.get_data()
robot2.get_data()

# Task 2

print('-' * 10, 'Task 2:', sep='\n')


class Counter:
    def set(self, value=1):
        self.count = value

    def plus(self):
        self.count += 1

    def get(self):
        return self.count


x = Counter()
y = Counter()

x.set(100)
x.plus()

y.set()

print('Result:', y.get())
print('Result:', x.get())
