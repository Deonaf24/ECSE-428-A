from src.engine import Engine
from src.errors import STACK_UNDERFLOW

# T-PUSH-REAL1
def test_push_real_then_pop_prints_canonical():
    c = Engine()
    c.execute("push 5")
    assert c.execute("pop") == "5 + j0"

#T-POP-ERR1
def test_pop_stack_underflow():
    c = Engine()
    try:
        c.execute("pop")
        assert False, "Expected stack underflow"
    except Exception as e:
        assert str(e) == STACK_UNDERFLOW