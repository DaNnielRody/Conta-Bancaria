
class BankAccount:

    def __init__(self, initial_balance, account_id):
        self.balance = initial_balance
        self.id = account_id
        self.daily_withdraw = 0
        self.max_withdraw = 500.00
        self.transactions = []

    def deposit(self, deposit_amount: float) -> float:

        if deposit_amount <= 0:
            raise ValueError("Por favor, deposite um valor válido.")

        self.balance += deposit_amount
        self.transactions.append({"type": "deposit", "amount": deposit_amount})

        return self.balance

    def withdraw(self, withdraw_amount: float) -> float:

        if withdraw_amount > self.balance or withdraw_amount <= 0 or withdraw_amount >= self.max_withdraw:
            raise ValueError("Por favor, saque um valor válido.")
        elif self.daily_withdraw >= 3:
            raise ValueError("Limite de saques atingido! Volte amanhã.")

        self.balance -= withdraw_amount
        self.daily_withdraw += 1
        self.transactions.append({"type": "withdraw", "amount": withdraw_amount})

        return self.balance

    def show_extract(self):
        for transaction in self.transactions:
            print(f"Tipo: {transaction['type']}, Valor: {transaction['amount']:.2f}")

    def show_balance(self):
        print(f"R$: {self.balance:.2f}")


my_bank_account = BankAccount(500, 1)
my_bank_account.deposit(500)
my_bank_account.show_balance()
my_bank_account.withdraw(200)
my_bank_account.withdraw(200)
my_bank_account.withdraw(200)
my_bank_account.show_balance()
my_bank_account.show_extract()
