# social_network.py
from user import User

class SocialNetwork:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name in self.users:
            print(f"User '{name}' already exists.")
        else:
            self.users[name] = User(name)
            print(f"User '{name}' added to the network.")

    def get_user(self, name):
        return self.users.get(name, None)

    def display_network(self):
        print("\nSocial Network Overview:")
        for user in self.users.values():
            print(user)
        print()
