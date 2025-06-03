# Basic test to ensure functions exist
from pomodoro import timer

def test_functions_exist():
    assert callable(timer.countdown)
    assert callable(timer.pomodoro_cycle)
