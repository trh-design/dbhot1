from functools import wraps   

def requires_aurth(f):
    @wraps(f)
    def decoratoed(*arg, **kwarps):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*arg, **kwarps)
    return decoratoed