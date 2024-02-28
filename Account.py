class Account:
    _instance = None

    def __new__(cls, balance, account_number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.balance = balance
            cls._instance.account_number = account_number
        return cls._instance

    def __init__(self, balance, account_number):
        pass