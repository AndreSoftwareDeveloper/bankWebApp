class Account:

    def __init__(self, balance: int, account_number: int, history, owner, login, password, transactions_history):
        self.balance = balance
        self.account_number = account_number
        self.login = login
        self.password = password
        self.transactions_history = transactions_history
        self.history = history
        self.owner = owner
