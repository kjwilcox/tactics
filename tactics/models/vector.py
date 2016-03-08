import pyrsistent


def Vector2(x, y):
    return pyrsistent.m(x=x, y=y)
