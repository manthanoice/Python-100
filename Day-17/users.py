class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0
        self.likes = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    def like(self, user):
        user.likes += 1

user1 = User(12, "Mikasa")
user2 = User(11, "Eren")
user1.follow(user2)
user1.like(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
print(user1.likes)
print(user2.likes)