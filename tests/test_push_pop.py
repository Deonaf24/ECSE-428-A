from src.engine import Engine

# T-PUSH-REAL1
def test_push_real_then_pop_prints_canonical():
    c = Engine()
    c.execute("push 5")
    assert c.execute("pop") == "5 + j0"