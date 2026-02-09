from src.engine import Engine

# T-SUB-REAL1
def test_sub_real_then_pop():
    c = Engine()
    c.execute("push 5")
    c.execute("push 2")
    c.execute("sub")
    assert c.execute("pop") == "3 + j0"
