# main.py
from network_manager_module import SocialNetwork

def main():
    network = SocialNetwork()

    while True:
        print("\n--- Social Network Simulation ---")
        print("1. Add User")
        print("2. Add Friend")
        print("3. Post Message")
        print("4. Like a Post")
        print("5. View User Posts")
        print("6. Display Network")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter the user's name: ")
            network.add_user(name)

        elif choice == "2":
            user1 = input("Enter the name of the first user: ")
            user2 = input("Enter the name of the second user: ")
            u1 = network.get_user(user1)
            u2 = network.get_user(user2)
            if u1 and u2:
                u1.add_friend(u2)
                print(f"{user1} and {user2} are now friends.")
            else:
                print("One or both users do not exist.")

        elif choice == "3":
            user = input("Enter the user's name: ")
            u = network.get_user(user)
            if u:
                message = input("Enter the message: ")
                u.post_message(message)
            else:
                print("User does not exist.")

        elif choice == "4":
            liker = input("Enter the name of the user liking the post: ")
            author = input("Enter the name of the user whose post is being liked: ")
            u_liker = network.get_user(liker)
            u_author = network.get_user(author)
            if u_liker and u_author:
                u_author.view_posts()
                try:
                    post_index = int(input("Enter the post number to like: ")) - 1
                    u_liker.like_post(u_author, post_index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("One or both users do not exist.")

        elif choice == "5":
            user = input("Enter the user's name: ")
            u = network.get_user(user)
            if u:
                u.view_posts()
            else:
                print("User does not exist.")

        elif choice == "6":
            network.display_network()

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
