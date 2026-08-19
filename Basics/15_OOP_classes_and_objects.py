import os #import used in Task 3

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
    def __init__(self, count):
        self.count = count

    def plus(self):
        self.count += 1

    def get(self):
        return self.count

    def __str__(self):
        return str(self.count)


x = Counter(100)
y = Counter(111)

x.plus()

print('Result:', y)
print('Result:', x)

# Task 3

print('-' * 10, 'Task 3:', sep='\n')


class Path:
    def __init__(self, path=None):
        self.CWD = os.getcwd()
        self.current = path or os.path.dirname(__file__)

    def parent(self):
        self.current = os.path.dirname(self.current)
        return self

    def get_parent(self):
        return os.path.dirname(self.current)

    def add_dir(self, dirname):
        self.current = os.path.join(self.current, dirname)
        return self

    def get_path(self):
        return self.current

    def __str__(self):
        return str(self.current)


path = Path().parent().add_dir('Test')

print('Directory:', path.current)

# Task 4

print('-' * 10, 'Task 4:', sep='\n')


class Path:
    def __init__(self, path=None):
        self.current = path or os.path.dirname(__file__)

    def parent(self):
        self.current = os.path.dirname(self.current)
        return self

    def get_path(self):
        return self.current

    def __add__(self, obj):
        return Path(os.path.join(self.current, obj))

    def __radd__(self, obj):
        return Path(os.path.join(self.current, obj))

    def __len__(self):
        return len(self.current)

    def __bool__(self):
        return bool(len(self.current))

    def __eq__(self, obj):
        return self.current == obj.current

    def __ne__(self, obj):
        return NotImplemented

    def __lt__(self, obj):
        return self.current < obj.current

    def __gt__(self, obj):
        return NotImplemented

    def __le__(self, obj):
        return self.current <= obj.current

    def __ge__(self, obj):
        return self.current >= obj.current

    def __contains__(self, obj):
        return obj in self.current

    def __fspath__(self):
        return str(self)

    def __str__(self):
        return self.current


path = Path('test\\my\\object')
path2 = Path('test\\my')

print('Directory:', path)
print('New directory:', os.path.join(path, 'home'))
print('test' in path)

# Task 5

print('-' * 10, 'Task 5:', sep='\n')


class Palette:
    red = '31'
    green = '32'
    yellow = '33'
    blue = '34'

    def __getattribute__(self, name):
        print('getattribute')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print('getattr')
        self.__dict__[name] = None
        return None

    def __setattr__(self, name, value):
        print('setattr')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(name)


obj = Palette()
color = obj.red

print(f'\033[{color}mRed text\033[0m')

obj.new = 25

print(obj.__dict__)

del obj.new

print(obj.__dict__)
