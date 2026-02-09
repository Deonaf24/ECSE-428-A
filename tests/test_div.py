import pytest
from src.engine import Engine
from src.errors import STACK_UNDERFLOW, DIVISION_BY_ZERO

# T-DIV-REAL1
def test_div_real1():
    """T-DIV-REAL1: Divide two real numbers (8 / 2 = 4)"""
    engine = Engine()
    engine.execute("push 8")
    engine.execute("push 2")
    engine.execute("div")
    result = engine.execute("pop")
    assert result == "4 + j0"