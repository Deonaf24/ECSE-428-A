import pytest
from src.engine import Engine
from src.errors import STACK_UNDERFLOW

# T-MUL-REAL1
def test_mul_real1():
    """T-MUL-REAL1: Multiply two real numbers (3 * -2 = -6)"""
    engine = Engine()
    engine.execute("push 3")
    engine.execute("push -2")
    engine.execute("mul")
    result = engine.execute("pop")
    assert result == "-6 + j0"

#T-MUL-CPLX1
def test_mul_cplx1():
    """T-MUL-CPLX1: Multiply two complex numbers (1+j2) * (3-j4) = 11+j2"""
    engine = Engine()
    engine.execute("push 1+j2")
    engine.execute("push 3-j4")
    engine.execute("mul")
    result = engine.execute("pop")
    assert result == "11 + j2"