from src.engine import Engine
from src.errors import STACK_UNDERFLOW

# T-ADD-REAL1
def test_add_real_then_pop():
    c = Engine()
    c.execute("push 2")
    c.execute("push 5")
    c.execute("add")
    assert c.execute("pop") == "7 + j0"

# T-ADD-CPLX1
def test_add_complex_then_pop():
    c = Engine()
    c.execute("push 3+j4")
    c.execute("push 1-j2")
    c.execute("add")
    assert c.execute("pop") == "4 + j2"

# T-ADD-ERR1
def test_add_underflow_errors():
    c = Engine()
    c.execute("push 3")
    try:
        c.execute("add")
        assert False, "Expected stack underflow"
    except Exception as e:
        assert str(e) == STACK_UNDERFLOW
