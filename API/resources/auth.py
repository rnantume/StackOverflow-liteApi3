from API.models.allmodels import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password==password:
        return user

def identity(payload):
    userId = payload['identity']
    return User.find_by_userId(userId)