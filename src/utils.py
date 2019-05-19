"""
For creating all arrays with the same dtype/precision
to keep memory constant.
"""

import numpy as np

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
