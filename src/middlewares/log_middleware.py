from functools import wraps


def log_request(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('Uma requisição rolou aqui')
        return f(*args, **kwargs)
    return decorated_function
