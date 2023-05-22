class BankAccount:

    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance

    def add_money(self, rubles):
        self.balance += rubles

    def dec_money(self, rubles):
        self.balance -= rubles


student = BankAccount('Иван', 20000, 5000)
student.add_money(1000)
student.dec_money(300)
print(student.balance)
