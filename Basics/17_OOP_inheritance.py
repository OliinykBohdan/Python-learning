# Task 1

print('-' * 10, 'Task 1:', sep='\n')


class Bild:
    def __init__(self, years, city):
        self.years = years
        self.city = city
        self.get_info()

    def get_info(self):
        print('Year:', self.years, 'City:', self.city)


class School(Bild):
    def __init__(self, years, city, pupils):
        super(School, self).__init__(years, city)
        self.pupils = pupils


class House(Bild):
    pass


class Shop(Bild):
    pass


school = School(1973, 'Dnipro', 500)
house = Bild(1985, 'Kyiv')
shop = Bild(1999, 'Odesa')

# Task 2

print('-' * 10, 'Task 2:', sep='\n')


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        return f'{self.first_name} {self.last_name}, age {self.age}'


class Salary_Mixin:
    def change_salary(self, new):
        self.salary = new


class Kid(Person):
    pass


class Adult(Person):
    def __init__(self, first_name, last_name, age, salary=None):
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def introduce(self):
        return super().introduce() + \
            f', salary: {self.salary}$'


class Customer(Person):
    name = 'Customer'


class Employee(Salary_Mixin, Adult):
    name = 'Employee'


class Employer(Salary_Mixin, Adult):
    pass


class Employee_Cust(Employee, Customer):
    pass


person = Employee_Cust('John', 'Doe', 35)

print(person.introduce())
print(Employee_Cust.__mro__)
