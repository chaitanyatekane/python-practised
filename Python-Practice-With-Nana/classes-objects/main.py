from user import User
from post import Post

app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_one.change_password("Chaitu")
app_user_two = User("aa@aa.com", "James Bond", "supersecret", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()


# Sample Output :-
# User Nana Janashia currently works as a DevOps Engineer. You can contact them at nn@nn.com
# New Password :- Chaitu!
# User James Bond currently works as a Agent. You can contact them at aa@aa.com
# Post: on a secret mission today written by James Bond
