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
            #push <token>  OR  push <a> <+|-> j <b>
            if len(args) == 2:
                token = args[1]
            elif len(args) == 5 and args[2] in {"+", "-"} and args[3].lower() == "j":
                token = f"{args[1]}{args[2]}j{args[4]}"  # "3+j4" or "3-j4"
            else:
                raise Exception(INVALID_TOKEN)

            try:
                r, i = _parse_number(token)
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
        
        elif cmd == "add":
            # need two values on stack
            if len(self.stack.data) < 2:
                raise Exception(STACK_UNDERFLOW)

            x_r, x_i = self.stack.pop()
            y_r, y_i = self.stack.pop()

            self.stack.push((y_r + x_r, y_i + x_i))
            return None


        elif cmd == "mul":
            if len(self.stack.data) < 2:
                raise Exception(STACK_UNDERFLOW)
            x = self.stack.pop()
            y = self.stack.pop()

            real = y[0] * x[0] - y[1] * x[1]
            imag = y[0] * x[1] + y[1] * x[0]

            self.stack.push((real, imag))
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


        