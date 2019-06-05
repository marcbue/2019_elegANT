"""
For creating all arrays with the same dtype/precision
to keep memory constant.
"""

import numpy as np
from time import time
from functools import wraps

dtype = np.float32


def array(*args, **kwargs):
    kwargs.setdefault('dtype', dtype)
    return np.array(*args, **kwargs)


def zeros(*args, **kwargs):
    kwargs.setdefault('dtype', dtype)
    return np.zeros(*args, **kwargs)


def empty(*args, **kwargs):
    kwargs.setdefault('dtype', dtype)
    return np.zeros(*args, **kwargs)


def ones(*args, **kwargs):
    kwargs.setdefault('dtype', dtype)
    return np.zeros(*args, **kwargs)


def uniform(*args, **kwargs):
    return np.random.uniform(*args, **kwargs).astype(dtype)


def randint(*args, **kwargs):
    if kwargs.get('size', 1) == 1:
        return np.random.randint(*args, **kwargs)
    else:
        return np.random.randint(*args, **kwargs).astype(dtype)


def random(*args, **kwargs):
    return np.random.random(*args, **kwargs).astype(dtype)


def get_objects_of_type(list_objects, target_type):
    sublist = []
    for obj in list_objects:
        if type(obj) == target_type:
            sublist.append(obj)
    return sublist


def timing(f):
    """
    Attributed to яүυк from Stackexchange.
    Prints the time a function needed to execute.
    :param f: function
    :return:
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Time: {} : {}'.format(f.__name__, end - start))
        return result

    return wrapper
