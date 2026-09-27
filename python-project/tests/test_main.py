from python_project.main import greeting


def test_greeting_uses_name() -> None:
    assert greeting("Ada") == "Hello, Ada!"


def test_greeting_defaults_for_blank_name() -> None:
    assert greeting("   ") == "Hello, World!"