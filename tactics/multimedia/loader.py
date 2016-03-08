import os

import pyglet

_loader = None


def get_loader():
    global _loader
    if not _loader:
        _loader = pyglet.resource.Loader(
            script_home=os.path.dirname(
                os.path.abspath(__file__)
            ),
            path=[
                'assets/images/tiles',
                'assets/images/units',
            ],
        )
        _loader.reindex()

    return _loader


def load_image(path):
    return get_loader().image(path)