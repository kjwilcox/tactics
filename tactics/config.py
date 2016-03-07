import pyrsistent


TARGET_FRAMERATE = 60
TICK_RATE = 1 / TARGET_FRAMERATE  # Frame time, in seconds

TILE_SIZE = 16
MAP_SIZE = pyrsistent.m(x=32, y=18)
