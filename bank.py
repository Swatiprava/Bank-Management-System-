# bank.py
import json
import random
import string
from pathlib import Path


class Bank:
    database = Path("data.json")
    data = []

    @classmethod
    def load_data(cls):
        if cls.database.exists():
            with open(cls.database, "r") as file:
                try:
                    cls.data = json.load(file)
                except json.JSONDecodeError:
                    cls.data = []
        else:
            cls.data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as file:
            json.dump(cls.data, file, indent=4)

    @staticmethod
    def __generate_account_number():
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("$%^&*#", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return ''.join(acc)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be 18+ and PIN must be 4 digits."

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": cls.__generate_account_number(),
            "balance": 0
        }

        cls.data.append(account)
        cls.__update()
        return True, account

    @classmethod
    def find_user(cls, account_no, pin):
        return next((user for user in cls.data if user['accountNo.'] == account_no and user['pin'] == pin), None)

    @classmethod
    def deposit(cls, account_no, pin, amount):
        user = cls.find_user(account_no, pin)
        if not user:
            return False, "Invalid account or PIN."
        if not (0 < amount <= 10000):
            return False, "Amount must be between 1 and 10000."

        user['balance'] += amount
        cls.__update()
        return True, user['balance']

    @classmethod
    def withdraw(cls, account_no, pin, amount):
        user = cls.find_user(account_no, pin)
        if not user:
            return False, "Invalid account or PIN."
        if user['balance'] < amount:
            return False, "Insufficient balance."

        user['balance'] -= amount
        cls.__update()
        return True, user['balance']

    @classmethod
    def get_details(cls, account_no, pin):
        user = cls.find_user(account_no, pin)
        if not user:
            return False, "Invalid account or PIN."
        return True, user

    @classmethod
    def update_details(cls, account_no, pin, name=None, email=None, new_pin=None):
        user = cls.find_user(account_no, pin)
        if not user:
            return False, "Invalid account or PIN."

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            user['pin'] = new_pin

        cls.__update()
        return True, "Details updated."

    @classmethod
    def delete_account(cls, account_no, pin):
        user = cls.find_user(account_no, pin)
        if not user:
            return False, "Invalid account or PIN."

        cls.data.remove(user)
        cls.__update()
        return True, "Account deleted."
