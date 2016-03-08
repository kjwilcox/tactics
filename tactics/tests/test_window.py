from flexmock import flexmock

from tactics.multimedia import window as module


def test_get_window_uses_cached_window():
    mock_window = flexmock()
    flexmock(module).should_receive("_window").and_return(mock_window)

    actual_window = module.get_window()

    assert mock_window == actual_window
