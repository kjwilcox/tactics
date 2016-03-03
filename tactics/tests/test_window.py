from tactics import window as module

import flexmock


def test_get_window_uses_cached_window():
    mock_window = flexmock()
    flexmock(module, _window=mock_window)

    actual_window = module.get_window()

    assert mock_window == actual_window
