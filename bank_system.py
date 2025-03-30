"""Банковсквя система."""


class BankAccount:
    """Создание класса аккаунта пользователя."""

    def __init__(self, account_number, account_holder, balance):
        """Инициализируем атрибуты класса BankAccount."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Добавление денег на счёт."""
        self.balance += amount
        print(f"Положено еще {amount}. Новый баланс: {self.balance}.")
        return ""

    def withdraw(self, amount):
        """Снятие денег."""
        balik = self.balance

        if balik - amount < 0:
            print("Операция невозможна")
        elif balik - amount >= 0:
            self.balance -= amount
            print(f"""С вашего счета была снята сумма {amount}, на вашем счету
теперь {self.balance}.""")
        else:
            print("Операция невозможна, Ошибка!")
        return ""

    def display_balance(self):
        """Отображает баланс пользователя."""
        print(f"На вашем счету сейчас {self.balance}")
        return ""


account = BankAccount("123542asdsa3", "Sergey Brnov", 221334312)

print(account.account_holder)
print(account.account_number)
print(account.balance)

print(account.deposit(102321))
print(account.withdraw(1000000000))
print(account.withdraw(10000))
print(account.display_balance())
