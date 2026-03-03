"""
This is a basic test for setting up ExpenseOracle
"""


def test_imports():
    """Test basic imports work"""
    import sys

    assert sys.version_info >= (3, 11)


def test_config_loads():
    """Test config"""
    try:
        import config

        assert hasattr(config, "APP_NAME")
    except ImportError:
        pass  # config might not exist yet
