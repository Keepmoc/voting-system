# -*- coding: utf-8 -*-
import csv
from user import User
from candidate import Candidate

class Voting:
    def __init__(self):
        self.load_data()
        
    def __exit__(self):
        self.save_data()
        
    def login(self, account, password):
        return User.login(account, password)
    
    def register_normal(self, account, name, password):
        return self.add_user(account, name, password, 'normal')
    
    def register_special(self, account, name, password):
        return self.add_user(account, name, password, 'candidate')
    
    def add_user(self, account, name, password, role):
        return User.add_user(account, name, password, role, 0)

    def add_candidate(self, name):
        data = None
        for key, user in User.users.items():
            if user.name == name and user.role == 'candidate':
                data = user
                break
        
        if data:
            return Candidate.add_candidate(name)
        else:
            print(f"This account {name} has no permissions.")
            return False
    
    def remove_user(self, account, password):
        return User.remove_user(account, password)
    
    def remove_candidate(self, name):
        return Candidate.remove_candidate(name)
    
    def query_candidate(self):
        return Candidate.query_candidate()
    
    def query_user(self):
        return User.users
    
    def cast_vote(self, account, name):
        return Candidate.cast_vote(account, name)
    
    def search_candidate(self, name):
        return Candidate.search_candidate(name)
    
    def search_user(self, name):
        return User.search_user(name)
    
    def load_data(self):
        user_path = 'database/user.csv'
        with open(user_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                User(row['Account'], row['Name'], row['Password'], row['Role'], row['Type'])
            
        candidate_path = 'database/candidate.csv'
        with open(candidate_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Candidate(row['Name'],row['Vote'])

    def save_data(self):
        user_path = 'database/user.csv'
        with open(user_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Account', 'Name', 'Password', 'Role', 'Type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for account, user in User.users.items():
                writer.writerow({
                    'Account': user.account,  
                    'Name': user.name,
                    'Password': user.password,  
                    'Role': user.role,
                    'Type': user.userType
                    })
        
        candidate_path = 'database/candidate.csv'
        with open(candidate_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Name', 'Vote']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for name, candidate in Candidate.candidates.items():
                writer.writerow({ 
                    'Name': candidate.name,
                    'Vote': candidate.vote, 
                    })
        
if __name__ == '__main__':
    pass