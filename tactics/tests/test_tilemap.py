from tactics import tilemap as module


def test_tilemap_loads_resources_and_does_not_raise():
    import pyglet
    pyglet.options['shadow_window'] = False
    module.TileMap(16, 16, 16)
