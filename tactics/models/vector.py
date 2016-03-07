import pyrsistent


def Vector2(x, y):
    return pyrsistent.m(x=x, y=y)


def Vector3(x, y, z):
    return pyrsistent.m(x=x, y=y, z=z)