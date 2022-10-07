class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance = 0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}\nBalance of account ({self.account_number}): S/ {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit was added")

    def retirar(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Retiro successfully")
        else:
            print("Is not suficient")


def create_customer():
    first_name_customer = input("Enter your name: ")
    last_name_customer = input("Enter your last name: ")
    account_number = input("Enter your account number: ")
    return Customer(first_name_customer, last_name_customer, account_number)

def init():
    my_customer = create_customer()
    print(my_customer)
    option = 0

    while option != 'S':
        print("Choice: Depositar (D), Retirar (R), Salir (S)")
        option = input("Ingrese opción: ")

        if option == 'D':
            amount = int(input("Monto a depositar: "))
            my_customer.deposit(amount)
        elif option == 'R':
            amount = int(input("Monto a retirar: "))
            my_customer.retirar(amount)

        print(my_customer)

    print("Thanks!!!")


init()