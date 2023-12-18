""" 1.  Create a Python class representing a "Car." Define attributes such as make, model, and year. Include methods to display information about the car.
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        

# car1 = Car("Toyota" , "Prius" , 2016)
# car1.display()


"""
2. Extend the "Car" class from Exercise 1 to create a new class, "ElectricCar." Add attributes specific to electric cars, such as battery_capacity and methods related to electric car features.
"""
class ElectricCar(Car):
    def __init__(self, make, model, year , battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
    def display(self):
        super().display()
        print (f"Battery Capacity: {self.battery_capacity}")

# electric_car1 = ElectricCar("Tesla", "S" , 2018, "100kw")
# electric_car1.display()
"""
3. Design a class representing a "BankAccount." Implement methods for deposit, withdrawal, and displaying the balance. Use encapsulation to protect the balance attribute.
""" 
class BankAccount:
    def __init__ (self, name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance 
        print("Account Created.")
    def deposit(self, money):
        if money > 0:
            self.__balance += money
            print (f"Your account is credited with {money}. You are remaining {self.__balance} Birr.")
        else: print ("Invalid deposit ammount.")
    def withdrawal(self, money):
        if money < self.__balance:
            self.__balance -= money
            print (f"Your account is debited with {money}. You are remaining {self.__balance} Birr.") 
    def display(self):
        print (f"You have {self.__balance} in your account.")

# acc = BankAccount("Robel" , 12345677)
# acc.deposit(2000)
# acc.withdrawal(1000)
# acc.display()
"""
4. Create a class hierarchy for geometric shapes, such as "Circle," "Rectangle," and "Triangle." Implement a method calculate_area in each class. Demonstrate polymorphism by calling calculate_area on different shape objects.
""" 
class Shape:
    def calculate_area():
        pass
class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__ (self, length , width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def __init__ (self, base , height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return self.base * self.height / 2
# cir = Circle(4)
# rec = Rectangle (4 , 5)
# tri = Triangle (4 , 5)
# for x in (cir , rec , tri):
#     print(x.calculate_area())


"""
5. Write unit tests for the "BankAccount" class from Exercise 3. Test deposit, withdrawal, and balance-related methods to ensure they behave as expected. """
import unittest

class TestBankAccountMethodes(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Robel Sisay","12345", 50)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account._BankAccount__balance, 100) 
        self.account.deposit(-20) #negative number
        self.assertEqual(self.account._BankAccount__balance, 100) 

    def test_withdrawal(self):

        self.account.withdrawal(30)
        self.assertEqual(self.account._BankAccount__balance, 20)  
        self.account.withdrawal(100) # more than the balance
        self.assertEqual(self.account._BankAccount__balance, 20) 

if __name__ == '__main__':
    unittest.main()
