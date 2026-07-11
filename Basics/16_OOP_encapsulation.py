class MyClass:
    def __init__(self):
        self.__private = 10
        self.public = 20

    def some_method(self):
        return self.__private + self.public

    def __private_method(self):
        print('This is private method')


a = MyClass()

print(a.public)
# print(a.__private)
# a.__private_method()
print(a.some_method())
