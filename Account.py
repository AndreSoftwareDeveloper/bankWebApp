class Account:
    _instance = None

    def __new__(cls, balance: int, account_number: int, history, owner):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.balance = balance
            cls._instance.account_number = account_number
            cls._instance.history = history
            cls._instance.owner = owner

        return cls._instance

    def __init__(self, balance, account_number, history, owner):
        pass
