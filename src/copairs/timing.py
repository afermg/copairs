import time
from functools import wraps

def timing(f):
    """
    A decorator that prints the execution time and arguments of a function.

    Parameters
    ----------
    f : callable
        The function to be decorated.

    Returns
    -------
    wrap : callable
        The decorated function.

    Notes
    -----
    This decorator uses the `time` module to calculate the execution time.
    """
    @wraps(f)
    def wrap(*args, **kw):
        """
        A wrapper function that calculates the execution time and prints it.

        Parameters
        ----------
        *args : tuple
            Variable number of positional arguments.
        **kw : dict
            Variable number of keyword arguments.

        Returns
        -------
        result : any
            The result of the decorated function.
        """
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        args_to_print = list(args)
        args_to_print = [len(x) if len(str(x)) > 4 else x for x in args]

        print(
            "func:%r args:[%s, %r] took: %2.4f sec"
            % (f.__name__, args_to_print, kw, te - ts)
        )
        return result

    return wrap
