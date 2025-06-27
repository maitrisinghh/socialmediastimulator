# user.py
class User:
    def __init__(self, name):
        self.name = name
        self.friends = set()
        self.posts = []
        self.likes_received = 0

    def add_friend(self, friend):
        if friend != self:
            self.friends.add(friend)
            friend.friends.add(self)
        else:
            print(f"{self.name} cannot add themselves as a friend.")

    def post_message(self, message):
        self.posts.append({"message": message, "likes": 0})
        print(f"{self.name} posted: {message}")

    def like_post(self, user, post_index):
        if 0 <= post_index < len(user.posts):
            user.posts[post_index]["likes"] += 1
            user.likes_received += 1
            print(f"{self.name} liked {user.name}'s post: '{user.posts[post_index]['message']}'")
        else:
            print(f"Invalid post index for {user.name}'s posts.")

    def view_posts(self):
        print(f"\n{self.name}'s Posts:")
        for i, post in enumerate(self.posts):
            print(f"{i + 1}. {post['message']} (Likes: {post['likes']})")
        print()

    def __str__(self):
        friends_names = ", ".join(friend.name for friend in self.friends)
        return f"User: {self.name}, Friends: [{friends_names}], Posts: {len(self.posts)}, Likes Received: {self.likes_received}"
