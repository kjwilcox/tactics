from tactics.models import vector as module


def test_vector2_created_properly():
    v = module.Vector2(1, 2)
    assert v.x == 1
    assert v.y == 2
