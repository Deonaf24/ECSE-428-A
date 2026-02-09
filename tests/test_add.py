from src.engine import Engine

# T-ADD-REAL1
def test_add_real_then_pop():
    c = Engine()
    c.execute("push 2")
    c.execute("push 5")
    c.execute("add")
    assert c.execute("pop") == "7 + j0"
