import time
time.sleep(10)
import pytest

from unittest.mock import patch
def raise_error_on_input(prompt = None):
    raise ValueError("The student.py file should only contain the function definition. It cannot contain a function call to the function you implemented.")
with patch("builtins.input", new=raise_error_on_input):
    import student


@pytest.fixture
def fake_input(monkeypatch):
    def func(inputs):
        def input(prompt=None):
            return str(next(iterator))

        iterator = iter(inputs)
        monkeypatch.setattr('builtins.input', input)

    return func


@pytest.mark.timeout(1)
@pytest.mark.parametrize("name, expected", [
    ("John", "Hello, John!\n"),
    ("Fionnula", "Hello, Fionnula!\n"),
    ("Saoirse", "Hello, Saoirse!\n"),
])
def test_interactive_greet(fake_input, capsys, name, expected):
    fake_input([name])

    student.interactive_greet()

    captured = capsys.readouterr()
    actual = captured.out
    assert expected == actual


# @pytest.mark.timeout(1)
# def test_interactive_greet_calls_greet(monkeypatch, fake_input, capsys):
#     def fake_greet(name):
#         return f"Bye, {name}"

#     fake_input(["Hannibal"])
#     monkeypatch.setattr('student.greet', fake_greet)

#     student.interactive_greet()

#     captured = capsys.readouterr()
#     actual = captured.out
#     expected = "Bye, Hannibal\n"
#     assert expected == actual, "interactive_greet should rely on greet"
