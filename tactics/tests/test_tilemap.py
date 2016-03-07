import pyglet

from tactics import tilemap as module


def test_tilemap_loads_resources_and_does_not_raise():
    pyglet.resource.path = ['../assets/images/tiles']
    pyglet.resource.reindex()
    module.TileMap(16, 16, 16)
