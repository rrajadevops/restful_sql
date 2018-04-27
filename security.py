from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'raja', 'raajaa'),
    User(2, 'raj', 'raja')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    print (username, password)
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

    def authenticate(username, password):
        user = User.query.filter(User.username == username).scalar()
        if bcrypt.check_password_hash(user.password, password):
            return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)