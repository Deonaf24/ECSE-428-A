import pytest
from src.engine import Engine
from src.errors import STACK_UNDERFLOW

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

# T-DEL-ERR1
def test_del_err1():
    """T-DEL-ERR1: Delete on empty stack raises stack underflow"""
    engine = Engine()
    with pytest.raises(Exception) as exc_info:
        engine.execute("delete")
    assert str(exc_info.value) == STACK_UNDERFLOW