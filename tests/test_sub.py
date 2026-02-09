from src.engine import Engine
from src.errors import STACK_UNDERFLOW

# T-SUB-REAL1
def test_sub_real_then_pop():
    c = Engine()
    c.execute("push 5")
    c.execute("push 2")
    c.execute("sub")
    assert c.execute("pop") == "3 + j0"

# T-SUB-CPLX1
def test_sub_complex_then_pop():
    c = Engine()
    c.execute("push 3+j4")
    c.execute("push 1-j2")
    c.execute("sub")
    assert c.execute("pop") == "2 + j6"

# T-SUB-ERR1
def test_sub_underflow_errors():
    c = Engine()
    try:
        c.execute("sub")
        assert False, "Expected stack underflow"
    except Exception as e:
        assert str(e) == STACK_UNDERFLOW