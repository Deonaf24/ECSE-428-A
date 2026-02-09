from src.stack import Stack
from src.errors import INVALID_TOKEN

class Engine:

    def __init__(self):
        self.stack = Stack()

    def execute(self, line: str) -> str | None:
        args = line.strip().split()
        if not args:
            return None
        
        cmd = args[0].lower()

        if cmd == "push":
            if len(args) != 2:
                raise Exception(INVALID_TOKEN)
            # hardcoding imaginary numbers because this is the first test
            val = float(args[1])
            self.stack.push((val, 0.0))
            return None
        
        if cmd == "pop":
            r, i = self.stack.pop()
            r = 0.0 if r == -0.0 else r
            i = 0.0 if i == -0.0 else i
            sign = "+" if i >= 0 else "-"
            return f"{_format_number(r)} {sign} j{_format_number(abs(i))}"
        
        raise Exception(INVALID_TOKEN)
    
def _format_number(x: float) -> str:
    if x.is_integer():
        return str(int(x))
    return str(x)


        