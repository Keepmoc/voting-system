# -*- coding: utf-8 -*-
import hashlib

class User:
    users = {}
    
    def __init__(self, account, name, password, role, userType):
        self.account = account
        self.name = name
        self.password = password
        self.role = role
        self.userType = userType
        
        User.users[account] = self
    
    @staticmethod
    def add_user(account, name, password, role, userType):
        if account not in User.users:
            password_encode = hashlib.sha256(password.encode()).hexdigest()
            User(account, name, password_encode, role, userType)
            print(f"Account with {account} has add.")
            return True
        else:
            print(f"Account with {account} has exists.")
            return False
    
    @staticmethod
    def remove_user(account, password):
        if account in User.users:
            user = User.users[account]
            if hashlib.sha256(password.encode()).hexdigest() == user.password:
                del User.users[account]
                print(f"User with account {account} deleted successfully.")
                return True
            else:
                print("Incorrect password")
                return False
        else:
            print(f"User with account {account} does not exist.")
            return False
    
    @staticmethod
    def set_user_type(account, userType):
        if account in User.users:
            User.users[account].userType = userType
            print("The user type was set successfully")
            return True
        else:
            print(f"User with account {account} does not exist.")
            return False
    
    @staticmethod
    def search_user(name):
        for key, value in User.users.items():
            if value.name == name:
                return value
        
        return None
    
    @staticmethod
    def login(account, password):
        if account in User.users:
            user = User.users[account]
            password_encode = hashlib.sha256(password.encode()).hexdigest()
            if password_encode == user.password:
                return user
            else:
                return None
        else:
            return None
    
if __name__ == '__main__':
    pass