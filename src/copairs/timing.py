from functools import wraps
from time import time

import numpy as np

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        args_to_print = list(args)
        args_to_print = [len(x) if len(x)>4 else x for x in args]

        print(
            "func:%r args:[%r, %r] took: %2.4f sec"
            % (f.__name__, args_to_print, kw, te - ts)
        )
        return result

    return wrap
