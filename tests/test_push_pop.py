from src.stack import Stack

def test_push_pop():
    s = Stack()
    s.push(5)
    assert s.pop() == 5