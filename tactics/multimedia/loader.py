import functools
import os

import pyglet


@functools.lru_cache()
def get_loader():
    loader = pyglet.resource.Loader(
        script_home=os.path.dirname(
            os.path.abspath(__file__)
        ),
        path=[
            'assets/images/tiles',
            'assets/images/units',
        ],
    )
    loader.reindex()

    return loader


def load_image(path):
    return get_loader().image(path)
