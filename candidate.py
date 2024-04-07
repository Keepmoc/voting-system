# -*- coding: utf-8 -*-
from user import User

class Candidate:
    candidates = {}
    
    def __init__(self, name, vote):
        self.name = name
        self.vote = vote
        
        Candidate.candidates[name] = self
    
    @staticmethod
    def add_candidate(name):
        if name not in Candidate.candidates:
            Candidate(name, 0)
            print("Added Successfully")
            return True
        else:
            print(f"The candidates {name} has exist")
            return False
    
    @staticmethod
    def remove_candidate(name):
        if name in Candidate.candidates:
            del Candidate.candidates[name]
            print("Deleted Successfully")
            return True
        else:
            print(f"The candidates {name} don't exist")
            return False
    
    @staticmethod
    def query_candidate():
        return Candidate.candidates
    
    @staticmethod
    def search_candidate(name):
        for key, value in Candidate.candidates.items():
            if value.name == name:
                return value
        
        return None;
    
    @staticmethod
    def cast_vote(account, name):
        if account in User.users:
            if User.users[account].userType == 1:
                print(f"This account {account} has already voted")
                return False
            
            if name in Candidate.candidates:
                Candidate.candidates[name].vote = int(Candidate.candidates[name].vote) + 1
                User.set_user_type(account, 1)
                print("Vote successfully.")
                return True
            else:
                print(f"The candidates {name} don't exist")
                return False
        else:
            return False
        
    
if __name__ == '__main__':
    pass