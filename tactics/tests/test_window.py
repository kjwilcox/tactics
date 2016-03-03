from tactics import window as module

from flexmock import flexmock


def test_get_window_uses_cached_window():
    mock_window = flexmock()
    flexmock(module).should_receive("_window").and_return(mock_window)

    actual_window = module.get_window()

    assert mock_window == actual_window


def test_get_window_creates_window():
    mock_window = flexmock()
    flexmock(module).should_receive("_window").and_return(None)
    flexmock(module).should_receive("create_window").and_return(mock_window)

    actual_window = module.get_window()

    assert mock_window == actual_window
