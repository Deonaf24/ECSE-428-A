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

# T-DIV-CPLX1
def test_div_cplx1():
    """T-DIV-CPLX1: Divide two complex numbers (4+j2) / (1+j1) = 3-j1"""
    engine = Engine()
    engine.execute("push 4+j2")
    engine.execute("push 1+j1")
    engine.execute("div")
    result = engine.execute("pop")
    assert result == "3 - j1"