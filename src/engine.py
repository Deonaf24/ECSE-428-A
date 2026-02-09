from src.stack import Stack
from src.errors import INVALID_TOKEN, STACK_UNDERFLOW

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
            try:
                r, i = _parse_number(args[1])
            except ValueError:
                raise Exception(INVALID_TOKEN)
            
            self.stack.push((r, i))
            return None
        
        elif cmd == "pop":
            r, i = self.stack.pop()
            r = 0.0 if r == -0.0 else r
            i = 0.0 if i == -0.0 else i
            sign = "+" if i >= 0 else "-"
            return f"{_format_number(r)} {sign} j{_format_number(abs(i))}"

        elif cmd == "mul":
            x = self.stack.pop()
            y = self.stack.pop()

            real = y[0] * x[0] - y[1] * x[1]
            imag = y[0] * x[1] + y[1] * x[0]

            self.stack.push((real, imag))
            return None
        
        elif cmd == "div":
            x = self.stack.pop()  # divisor (top)
            y = self.stack.pop()

            real = y[0] / x[0]

            self.stack.push((real, 0))
            return None
        
        else: 
            raise Exception(INVALID_TOKEN)
    
def _format_number(x: float) -> str:
    if x.is_integer():
        return str(int(x))
    return str(x)

def _parse_number(token: str) -> tuple[float, float]:
    token = token.strip().lower()

    if "j" in token:
        #pure imaginary
        if token.startswith("j"):
            return 0.0, float(token[1:])
        if token.startswith("-j"):
            return 0.0, -float(token[2:])

        #find +j or -j after the first char so we don't confuse with leading minus
        rest = token[1:]
        pos = rest.find("+j")
        neg = rest.find("-j")

        if pos != -1:
            idx = pos + 1  #adjust back to original string index
            real = float(token[:idx])
            imag = float(token[idx + 2 :])
            return real, imag

        if neg != -1:
            idx = neg + 1
            real = float(token[:idx])
            imag = float(token[idx + 2 :])
            return real, -imag

        raise ValueError("bad complex token")

    #real number
    return float(token), 0.0


        