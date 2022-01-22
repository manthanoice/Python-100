class user:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def authentication(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@authentication
def create_blog_post(user):
    print('This is {}\'s new blog post'.format(user.name))

new_user = user('Manthan')
new_user.is_logged_in = True
create_blog_post(new_user)