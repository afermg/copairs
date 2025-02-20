"""Decorator to benchmark speed."""

from pathlib import Path

import time
from functools import wraps


def rmtree(f: Path):
    """Remove a directory recursively."""
    if f.is_file():
        f.unlink()
    elif f.exists():
        for child in f.iterdir():
            rmtree(child)
        f.rmdir()


def timing(f):
    """
    Print the execution time and arguments of a function.

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
        Wrap a function to calculate the execution time and print it.

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
        # Remove cache for proper timing
        rmtree(Path.home() / ".copairs")

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        args_to_print = list(args)
        args_to_print = [
            len(x) if hasattr(x, "__iter__") and len(x) > 4 else x for x in args
        ]

        print(
            "func:%r args:[%s, %r] took: %2.4f sec"
            % (f.__name__, args_to_print, kw, te - ts)
        )
        return result

    return wrap
