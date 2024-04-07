# -*- coding: utf-8 -*-
from voting import Voting

class VotingSystem:
    
    def __init__(self, Voting):
        self.voting = Voting
        self.user = None
        
    def run(self):
        while True:
            if self.user is None:
                
                print("\n----- Voting System -----")
                print("1. Login")  
                print("2. Register Student")  
                print("3. Registered Student Union Member")  
                print("4. Quit")
            
                choice = input("\nEnter your choice:")
            
                if choice == "1":
                    self.login()
                elif choice == "2":
                    self.register_normal()
                elif choice == "3":
                    self.register_special()
                elif choice == "4":
                    print("\nExiting the system...")
                    self.save_data()
                    return
                else:
                    print("\nInput error, Please try again.")  
            
            if self.user:
                while True:
                    print("\n")
                    print("1. View All Candidates")  
                    print("2. Search Candidates")  
                    print("3. Vote")  
                    print("4. Register as a candidate")
                    print("5. Managing Voter")
                    print("6. Managing Candidates")
                    print("9. Quit")
                
                    choice = input("\nEnter your choice:")
                
                    if choice == "1":
                        self.show_all_candidates()
                        break
                    elif choice == "2":
                        self.search_candidates()
                        break
                    elif choice == "3":
                        self.vote()
                        break
                    elif choice == "4":
                        self.add_candidate()
                        break
                    elif choice == "5":
                        self.manage_voter()
                        break
                    elif choice == "6":
                        self.manage_candidates()
                        break
                    elif choice == "9":
                        print("\nExiting the system...")
                        self.save_data()
                        return
                    else:
                        print("\nInvalid choice, Please try again.")
    
    def login(self):
        account = input("\nEnter your account:")
        password = input("\nEnter your password:")
        self.user = self.voting.login(account, password)
        print("\nLogin Success")
    
    def register_normal(self):
        account = input("\nEnter your account:")
        name = input("\nEnter your name:")
        password = input("\nEnter your password:")
        self.voting.register_normal(account, name, password)
    
    def register_special(self):
        account = input("\nEnter your account:")
        name = input("\nEnter your name:")
        password = input("\nEnter your password:")
        self.voting.register_special(account, name, password)  
    
    def show_all_candidates(self):
        candidates = self.voting.query_candidate()
        print("\nQuery results:")
        for key, candidate in candidates.items():
            print(f"\nName: {key}, Vote: {candidate.vote}")
    
    def search_candidates(self):
        name = input("\nEnter Candidates Name:")
        data = self.voting.search_candidate(name)
        if data:
            print(f"Name: {data.name}, Vote: {data.vote}")
        else:
            print(f"No candidate by that name:{name} exists")
    
    def show_all_user(self):
        users = self.voting.query_user()
        print("\nQuery results:")
        for key, user in users.items():
           print(f"\nAccount: {key}, Name: {user.name}")
    
    def search_user(self):
        name = input("\nEnter User Name:")
        data  = self.voting.search_user(name)
        if data:
            print(f"Account: {data.account}, Name: {data.name}")
        else:
            print(f"No user by that name:{name} exists")
    
    
    def remove_user(self):
        account = input("\nEnter User Account:")
        password = input("\nEnter User Pawword:")
        self.voting.remove_user(account, password)
        
    def remove_candidate(self):
        name = input("\nEnter Candidates Name:")
        self.voting.remove_candidate(name)    
    
    def vote(self):
        name = input("\nEnter Candidates Name:")
        account = self.user.account
        self.voting.cast_vote(account, name)
    
    def add_candidate(self):
        user = self.user
        self.voting.add_candidate(user.name)
    
    def manage_voter(self):
        if self.user.role == "Administrator":
            while True:
                print("1. View All Voter")  
                print("2. Search Voter")  
                print("3. Add Voter")  
                print("4. Remove Voter")  
                print("9. Quit")
                
                choice = input("\nEnter your choice:")
                
                if choice == "1":
                    self.show_all_user()
                    pass
                elif choice == "2":
                    self.search_user()
                    break
                elif choice == "3":
                    account = input("\nEnter your account:")
                    name = input("\nEnter your name:")
                    password = input("\nEnter your password:")
                    role = "normal"
                    self.voting.add_user(account, name, password, role)
                    break
                elif choice == "4":
                    self.remove_user()
                    break
                elif choice == "9":
                    return
                else:
                    print("\nInvalid choice, Please try again.")
        else:
            print(f"The user <{self.user.account}> has no permissions.")
        
            
    def manage_candidates(self):
        if self.user.role == "Administrator":
            while True:
                print("1. View All Candidates")  
                print("2. Search Candidates")  
                print("3. Add Candidates")  
                print("4. Remove Candidates")  
                print("9. Quit")
                
                choice = input("\nEnter your choice:")
                
                if choice == "1":
                    self.show_all_candidates()
                    pass
                elif choice == "2":
                    self.search_candidates()
                    break
                elif choice == "3":
                    self.add_candidate()
                    break
                elif choice == "4":
                    self.remove_candidate()
                    break
                elif choice == "9":
                    return
                else:
                    print("\nInvalid choice, Please try again.")
        else:
            print(f"The user <{self.user.account}> has no permissions.")    
    
    def save_data(self):
        self.voting.save_data()

if __name__ == '__main__':
    voting = Voting()
    cli = VotingSystem(voting)
    cli.run()