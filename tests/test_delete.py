import pytest
from src.engine import Engine

# T-DEL-REAL1
def test_del_real1():
    """T-DEL-REAL1: Delete top of stack with real numbers"""
    engine = Engine()
    engine.execute("push 1")
    engine.execute("push 2")
    engine.execute("delete")
    result = engine.execute("pop")
    assert result == "1 + j0"

# T-DEL-CPLX1
def test_del_cplx1():
    """T-DEL-CPLX1: Delete top of stack with complex numbers"""
    engine = Engine()
    engine.execute("push 1+j1")
    engine.execute("push 2+j3")
    engine.execute("delete")
    result = engine.execute("pop")
    assert result == "1 + j1"