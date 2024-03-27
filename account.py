from person import Person


class Account:
    def __init__(self, UserMixin, db,  account_number: int, password, balance: int, transactions_history, owner: Person):
        self.db_model = db.model
        # self.account_number = db.Column(db.String(100), unique=True, nullable=False)
        self.password = db.Column(db.String(100), nullable=False)
        self.balance = balance
        self.transactions_history = transactions_history
        self.owner = owner
